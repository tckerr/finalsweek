param(
    [string]$test_name = "create"
)

$TEST_ROOT = "$($PSScriptRoot)\test\"

switch ($test_name) {
    "create"    { & "$($TEST_ROOT)\create_single.ps1" }
    "load"      { & "$($TEST_ROOT)\load_single.ps1" }
    "stress"    { & "$($TEST_ROOT)\stress.ps1" }
}