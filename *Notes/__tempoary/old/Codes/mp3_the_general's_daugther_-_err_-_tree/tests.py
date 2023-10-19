import unittest

from FileDescriptor import FileDescriptor 
from GeneralTreeNode import (DirectoryNode, FileNode) 


root = DirectoryNode("/")
cmd  = FileDescriptor(root)
dirs    = ['bin', 'dev', 'home', 'opt', 'root', 'sbin', 'sys', 'usr',
           'boot', 'etc', 'mnt', 'proc', 'run', 'srv', 'tmp', 'var']
for name in dirs:
    cmd.mkdir(name)

class TestFileDescriptor(unittest.TestCase):
    def test_resolve_path(self):
        cmd.pwd = root
        self.assertNotEqual(cmd._resolve_path("."), None) 
        self.assertNotEqual(cmd._resolve_path("/"), None) 
        self.assertNotEqual(cmd._resolve_path("/home"), None) 
        self.assertNotEqual(cmd._resolve_path("home"), None) 
        self.assertNotEqual(cmd._resolve_path("home/.././tmp/."), None) 
        self.assertNotEqual(cmd._resolve_path("/home/.."), None) 
        self.assertNotEqual(cmd._resolve_path("/home/../bin/../etc///"), None) 
        self.assertNotEqual(cmd._resolve_path(".."), None) 
        self.assertNotEqual(cmd._resolve_path("/././././////"), None) 
        self.assertNotEqual(cmd._resolve_path("/././././////../../../"), None) 
        self.assertEqual(cmd._resolve_path("/home//./..//sd"), None)

    def test_cd(self):
        cmd.pwd = root
        self.assertEqual(cmd.cd("bin"), True)
        self.assertEqual(cmd.cd("/bin"), True)
        self.assertEqual(cmd.cd("../home"), True)
        self.assertEqual(cmd.cd("../././../tmp"), True)
        self.assertEqual(cmd.cd("./././../etc////"), True)
        self.assertEqual(cmd.cd("/./././../..///../sbin"), True)
        self.assertEqual(cmd.cd("/usr///"), True)
        self.assertEqual(cmd.cd("////proc"), True)
        self.assertEqual(cmd.cd("////aproc"), False)

    def test_rmdir(self):
        cmd.pwd = root
        self.assertEqual(cmd.rmdir("bin"), 0)
        self.assertEqual(cmd.rmdir("/../."), 4)
        self.assertEqual(cmd.rmdir("bin"), 2)
        

if __name__ == "__main__":
    unittest.main()
