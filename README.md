# Qt6.NET - Qt 6 for C#
A work in progress C# bindings for Qt6 that uses [rcalixte's](https://github.com/rcalixte) [libqt6c](https://github.com/rcalixte/libqt6c) libraries.

Currently, only the libqt6c NuGet dependency is buildable.

## Building Native Qt6C NuGet (Linux only for now)
Before building, the following packages will need to be installed:
* .NET packages - `dotnet-sdk-8.0`, `dotnet-runtime-8.0`
* Python modules - `Jinja2` (installable via `python3 -m pip install Jinja2`)
* Qt6 development packages - [Seen here](https://github.com/rcalixte/libqt6c?tab=readme-ov-file#linux-native).

Note that some of the package names may be differently named in each Linux distribution.

Once all packages have been installed, run the `create-qt6c-nuget.sh` file in the `./NuGet/Qt6C` folder.

Note: If you are running a Linux distribution other than Fedora, you will need to manually type in the version number of your Qt 6 libraries.
