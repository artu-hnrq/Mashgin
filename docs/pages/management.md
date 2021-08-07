## Development management
> During application development some tasks are repeatedly executed,
and most time they consist in run multiple commands in shell. 
> 
> [GNU Make][>1] is a command line tool that can help one into [DRY][-1],
organize execution management actions and make them flexible and shareable.

[-1]: https://en.wikipedia.org/wiki/Don't_repeat_yourself "Don't repeat yourself"
[>1]: https://www.gnu.org/software/make/ "GNU Make"

The following Make *targets* have been implemented
to facilitate the application development and execution processes management.

Run `make <target>` from your preferred shell to execute the referenced *target* task.

### General
| Target | description |
| --- | --- |
| help             | Show all available targets and their brief description |
| init             | Configure execution environment |
| clean            | Delete all generated files |
| veryclean        | Uninstall execution environment completely |

### Documentation
| Target | description |
| --- | --- |
| docs             | Build documentation |
| read             | Serve documentation |
| publish          | Publish documentation into Github Pages |
