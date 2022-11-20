import os
import subprocess
from pathlib import Path

from homn.exceptions import UnexpectedExitCodeError


class ShellResult:
    def __init__(
        self, script: str, out: str, err: str, combined: str, code: int
    ) -> None:
        self.script = "\n".join(line.strip() for line in script.split("\n"))
        self.out = out
        self.err = err
        self.all = combined
        self.code = code


class Shell:
    def __init__(self, executable_path: str = "/bin/bash") -> None:
        self.executable_path = executable_path

    def __call__(
        self,
        user_script: str,
        bash_args: str = "",
        expected_exit_codes: list[int] = None,
    ) -> ShellResult:
        if expected_exit_codes is None:
            expected_exit_codes = []
        result = self._execute(user_script, bash_args)
        if expected_exit_codes and result.code not in expected_exit_codes:
            raise UnexpectedExitCodeError(result.err)
        return result

    def _execute(self, script: str, bash_args: str) -> ShellResult:
        stdout = []
        stderr = []
        mix = []
        code = 0

        for script_line in script.split("\n"):
            if bash_args:
                script_line = (
                    f"{self.executable_path.strip()} {bash_args} {script_line}"
                )
            proc = subprocess.Popen(
                script_line.strip(),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                universal_newlines=True,
                shell=True,
                executable=self.executable_path.strip(),
            )

            this_out, this_err = proc.communicate()
            stdout.append(this_out)
            stderr.append(this_err)
            mix.append(this_out)
            mix.append(this_err)

            if proc.returncode != 0:
                code = proc.returncode

        return ShellResult(script, "".join(stdout), "".join(stderr), "".join(mix), code)


sh = Shell()
