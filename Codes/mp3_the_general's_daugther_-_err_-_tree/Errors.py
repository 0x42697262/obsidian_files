errors = {
        "mkdir"     : {
                        0 : True,
                        1 : "mkdir: cannot create directory '{}': File exists",
                        2 : "mkdir: cannot create directory ‘{}’: No such file or directory",
                },
        "rmdir"     : {
                        0 : True,
                        1 : "rmdir: failed to remove '{}': Directory not empty",
                        2 : "rmdir: failed to remove '{}': No such file or directory",
                        3 : "rmdir: Invalid argument",
                        4 : "rmdir: cannot delete root directory",
                        5 : "rmdir: failed to remove '{}': Not a directory",
            },
        "cd"        : {
                        0 : True,
                        1 : "cd: no such file or directory: {}",
                        2 : "cd: not a directory: {}"
                },
        "ls"        : {
                        1 : "ls: cannot access '{}': No such file or directory",
                },
        "mv"        : {
                        0 : True,
                        1 : "mv: cannot stat '{}': No such file or directory",
                        2 : "mv: cannot move '{}' to a subdirectory of itself, '{}/{}'",
                        3 : "mv: cannot overwrite non-directory '{destination}' with directory '{source}'",
                },
        "cp"        : {
                        0 : True,
                        1 : "cp: target '{}': No such file or directory",
                        2 : "cp: cannot copy a directory, '{}', into itself, '{}/{}'",
                },
        "rm"        : {
                        0 : True,
                        1 : "rm: cannot remove '{}': No such file or directory",
                },
        "show"      : {
                        0 : True,
                        1 : "show: target '{}': No such file or directory",
                },
        "edit"      : {
                        0 : True,
                        1 : "edit: target '{}': Not a file",
                        2 : "edit: target '{}': Parent directory does not exist",
                        3 : "edit: data input is empty",
                },
        }
