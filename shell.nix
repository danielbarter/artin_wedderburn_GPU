with (import <nixpkgs> {});

mkShell {

  buildInputs = [ cudatoolkit
                  nvtop
                ];

  # nvtop can't find shared libraries. Should be fixed in nvtop
  shellHook = ''
    LD_LIBRARY_PATH=$LD_LIBRARY_PATH:${pkgs.linuxPackages.nvidia_x11}/lib
   '';
}
