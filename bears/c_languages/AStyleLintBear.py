from coalib.bearlib.abstractions.Linter import linter

@linter(executable='astyle',
        output_format='corrected')
class AStyleLintBear:
    """
    Artistic Style is a source code indenter, formatter, 
    and beautifier for the C, C++, C++/CLI, Objective‑C,
    C# and Java programming languages. 
    
    For more information, consult <http://astyle.sourceforge.net/astyle.html>.
    """
    
    LANGUAGES = {"C, C++, Objective-C, C#, Java"}
    AUTHORS = {'The coala developers'}
    AUTHORS_EMAILS = {'coala-devel@googlegroups.com'}
    LICENSE = 'AGPL-3.0'
    CAN_DETECT = {'Formatting'}
    
    @staticmethod
    def create_arguments(filename, file, config_file):    
        return '--dry-run', filename
