param(
    [int]$Port = 8765,
    [string]$DataDir = (Join-Path $env:LOCALAPPDATA 'Fold\local-preview')
)

$ErrorActionPreference = 'Stop'
$runtimeCandidates = @((Join-Path $PSScriptRoot '.venv\Scripts\python.exe'))
$pyCommand = Get-Command py -ErrorAction SilentlyContinue
if ($pyCommand) {
    try {
        $py312Path = (& $pyCommand.Source -3.12 -c 'import sys; print(sys.executable)' 2>$null).Trim()
        if ($py312Path) { $runtimeCandidates += $py312Path }
    } catch { }
}
$pythonCommand = Get-Command python -ErrorAction SilentlyContinue
if ($pythonCommand) { $runtimeCandidates += $pythonCommand.Source }
$runtimeCandidates += Join-Path $env:USERPROFILE '.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe'
$runtimePath = $null
foreach ($candidatePath in ($runtimeCandidates | Select-Object -Unique)) {
    if (Test-Path -LiteralPath $candidatePath) {
        try {
            & $candidatePath -c 'import importlib.util, sys; sys.exit(0 if sys.version_info >= (3, 12) and importlib.util.find_spec("pypdf") else 1)' 2>$null
            if ($LASTEXITCODE -eq 0) { $runtimePath = $candidatePath; break }
        } catch { continue }
    }
}
if (-not $runtimePath) {
    Write-Host ''
    Write-Host 'Fold non trova un Python compatibile con pypdf.' -ForegroundColor Yellow
    Write-Host 'Esegui una volta questi comandi nella cartella del progetto:'
    Write-Host '  py -3.12 -m venv .venv'
    Write-Host '  .\.venv\Scripts\python.exe -m pip install -r requirements.txt'
    Write-Host 'Poi rilancia: .\Start-Fold.ps1 -Port 8766'
    Write-Host ''
    exit 1
}
Push-Location -LiteralPath $PSScriptRoot
try {
    Write-Host ('Runtime: ' + $runtimePath)
    & $runtimePath -m fold_app --port $Port --data-dir $DataDir
    exit $LASTEXITCODE
} finally {
    Pop-Location
}
