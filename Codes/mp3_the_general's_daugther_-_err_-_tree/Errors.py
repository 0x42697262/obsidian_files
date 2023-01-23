errors = {
        "mkdir"     : {
                        0 : True,
                        1 : "cannot create directory '{}': File exists",
                        2 : "cannot create directory ‘{}’: No such file or directory",
                },
        "rmdir"     : {
                        0 : True,
                        1 : "Directory not empty",
                        2 : "No such file or directory",
                        3 : "Invalid argument",
                        4 : "Cannot delete root directory",
                        5 : "Not a directory",
            },
        "cd"        : {
                        0: True,
                        1: "",
                        2: "Not a directory"
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
