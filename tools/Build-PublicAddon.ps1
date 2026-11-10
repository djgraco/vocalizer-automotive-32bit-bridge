param(
    [string]$RepositoryRoot = (Split-Path -Parent $PSScriptRoot),
    [string]$OutputDirectory = (Join-Path (Split-Path -Parent $PSScriptRoot) "dist")
)

$ErrorActionPreference = "Stop"
$repositoryRoot = (Resolve-Path -LiteralPath $RepositoryRoot).Path
$outputDirectory = [System.IO.Path]::GetFullPath($OutputDirectory)

& uv run --project $repositoryRoot --locked scons -C $repositoryRoot "outputDirectory=$outputDirectory"
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
& uv run --project $repositoryRoot --locked python (Join-Path $repositoryRoot "tools/check_project.py") --package --output-directory $outputDirectory --write-checksum
exit $LASTEXITCODE
