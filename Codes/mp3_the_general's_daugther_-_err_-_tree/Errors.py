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
                        0: True,
                        1: "cd: no such file or directory: {}",
                        2: "cd: not a directory: {}"
                },
        "ls"        : {
                        0 : True,
                        1 : "No such file or directory",
                },
        "mv"        : {
                        0 : True,
                        1 : "No such file or directory",
                        2 : "cannot move '{}' to a subdirectory of itself, '{}/{}'",
                        3 : "cannot overwrite non-directory '{destination}' with directory '{source}'",
                },
        }
