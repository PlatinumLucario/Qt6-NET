# This will generate the .csproj and create the NuGet for Qt6C
ziglocation=$(whereis zig)
if [[ "$ziglocation" != "zig: " ]]; then
    pushd ../../libqt6c
    zig build -Dlinkage=dynamic --prefix-lib-dir ../../NuGet/Qt6C/runtimes/linux-x64/native
    cp LICENSE ../NuGet/Qt6C/LICENSE
    cp README.md ../NuGet/Qt6C/README.md
    popd
    python3 ./qt6c-csproj-generator.py
    dotnet pack -c Release
fi
