from pygments.lexer import RegexLexer, bygroups
from pygments.token import *

__all__ = ['SyslogLexer']

class SyslogLexer(RegexLexer):
    name = 'syslog'
    aliases = ["syslog"]
    filenames = ["*.log", "messages", "syslog", "secure"]

    tokens = {
        'root': [
            (r'^(...\s+..)(\s+)(\d\d:\d\d:\d\d)(\s+)(\w+)(\s+)([\w-]+(?:\[\d+\])?:)(\s)',
             bygroups(Operator.Word, Text, Name.Builtin, Text, Name.Function, Text, String, Text)),
            (r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', String),
            (r'(?:root|failed|POSSIBLE BREAK-IN ATTEMPT!)', Error),
            (r'.', Number),
        ]
    }
