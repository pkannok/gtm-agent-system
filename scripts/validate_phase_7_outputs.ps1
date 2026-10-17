param(
    [string]$CheckedAt = "2026-10-16T00:00:00Z"
)

$ErrorActionPreference = "Stop"
$repoRoot = Split-Path -Parent $PSScriptRoot
$gptRoot = Join-Path $repoRoot "outputs\phase-7-fixture-gpt-tests\runs"
$cases = @(
    @(
        Get-ChildItem -LiteralPath $gptRoot -Directory | Sort-Object Name | ForEach-Object {
            @{ Name = $_.Name; Path = $_.FullName; Expected = "pass" }
        }
    )
    @{ Name = "valid-output-package"; Path = (Join-Path $repoRoot "examples\script-smoke-tests\valid-output-package"); Expected = "pass" }
    @{ Name = "bad-output-package"; Path = (Join-Path $repoRoot "examples\script-smoke-tests\bad-output-package"); Expected = "fail" }
)

if (@($cases | Where-Object { $_.Path -like "$gptRoot*" }).Count -eq 0) {
    throw "No direct child package directories were discovered under $gptRoot"
}

$results = foreach ($case in $cases) {
    $json = & python (Join-Path $repoRoot "scripts\validate_output_package.py") --package-dir $case.Path --checked-at $CheckedAt | Out-String
    $exitCode = $LASTEXITCODE
    $report = $json | ConvertFrom-Json
    $failedChecks = @($report.checks | Where-Object { $_.status -eq "fail" } | ForEach-Object { $_.check_id })
    [PSCustomObject]@{
        Package = $case.Name
        Expected = $case.Expected
        Actual = $report.validation_status
        Exit = $exitCode
        FailedChecks = ($failedChecks -join ", ")
        MatchesExpectation = ($report.validation_status -eq $case.Expected)
    }
}

$results | Format-Table -AutoSize
if (@($results | Where-Object { -not $_.MatchesExpectation }).Count -gt 0) {
    exit 1
}
