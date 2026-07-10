# autoproject_workspace_test

The **test-workspace template** of the
[PyAutoScientist](https://pyautoscientist.readthedocs.io) organism: the home
for regression, smoke and integration scripts — everything that exercises
the installed library end to end but teaches nothing.

The split it encodes: the library's `tests/` hold fast unit tests; the
workspace holds teaching scripts; **this repo** holds the cross-package and
end-to-end checks the organism's health layer runs (a curated
`smoke_tests.txt` subset gates releases — keep it small and fast, don't
promote every script into it).

```bash
pip install autoproject
python scripts/fit_quick.py
```

Part of the PyAutoScientist template family — copy it ("Use this
template") alongside
[PyAutoProject](https://github.com/PyAutoLabs/PyAutoProject) and
[autoproject_workspace](https://github.com/PyAutoLabs/autoproject_workspace).
