import pyperf
import runpy
import sys
import tempfile


sys.argv.pop(0)
path_string = sys.argv[0]


with tempfile.NamedTemporaryFile() as temporary_file:

    def _(Runner):
        def _Runner(*args, program_args=None, **kwargs):
            assert program_args is None

            _v_ = (
                "-m",
                "kernprof",
                "-l",
                "-p",
                path_string,
                "--prof-imports",
                "-o",
                temporary_file.name,
                path_string,
            )
            return Runner(*args, program_args=_v_, **kwargs)

        return _Runner

    pyperf.Runner = _(pyperf.Runner)
    runpy.run_path(path_string, run_name="__main__")
