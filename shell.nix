with (import <nixpkgs> {});

let
  python = let packageOverrides = self: super: {

    cupy = super.cupy.overridePythonAttrs (
      old: {
        version = "9.0.0";
        src = super.fetchPypi {
          version = "9.0.0";
          pname = "cupy";
          sha256 = "1w8095q9hqdyx76lnk4h4s18qk0ahgnqnlcnrmw2yvb7vaag8s26";};
      }
    );

  }; in python38.override {inherit packageOverrides;};

  pythonEnv = python.withPackages (
      ps: [ ps.cupy
          ]);

in mkShell {

  buildInputs = [ nvtop
                  pythonEnv
                ];

  # nvtop can't find shared libraries. Should be fixed in nvtop
  shellHook = ''
    LD_LIBRARY_PATH=$LD_LIBRARY_PATH:${pkgs.linuxPackages.nvidia_x11}/lib
   '';
}
