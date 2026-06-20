# 推送到 GitHub 的辅助脚本
# 用法: 先在 GitHub 创建空仓库(如 wc2026),然后运行此脚本
param(
    [Parameter(Mandatory=$true)]
    [string]$RepoUrl  # 例如 https://github.com/你的用户名/wc2026.git
)
$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot
git config user.email "codex@local"
git config user.name "Codex"
git branch -M main
git remote remove origin 2>$null
git remote add origin $RepoUrl
git push -u origin main
Write-Host "已推送到 $RepoUrl" -ForegroundColor Green
Write-Host "接下来在 GitHub 仓库 Settings -> Pages 选择 main 分支根目录, 几分钟后访问 https://用户名.github.io/wc2026/" -ForegroundColor Yellow
