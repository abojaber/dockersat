using System.Text.RegularExpressions;

namespace dump;
class Program
{
    static void Main(string[] args)
    {
        string stg = "\n#comments\nNUMBER_VALUE=123123\nxyz=\"\"\"\ndfsdfsdf\n\"\"\"\nSTRING_VALUE=String value 3434 with spaces.\nCONECTION_STRING=Server=localhost;Database=Source_DB;Trusted_Connection=True;TrustServerCertificate=True\nNOT_ENV_VALID_VARIABLE=\nMULTI_LINE_VARIABLE=\"\"\"\nThis is multi line\nSample Variable\n\"\"\"";
        
        
        Console.WriteLine(stg);
        Console.WriteLine("^^^^^^^^^^^^^^^^^^^^^^");
        
        var pattern_single_line = @"([a-zA-Z_]\w*)\s*=(?!""{2,})(.*?)(\n|$)";
        // var pattern_single_line = @"([a-zA-Z_]\w*)\s*=(?!""{2,}).*?(\n)";
            
            MatchCollection matches = Regex.Matches(stg, pattern_single_line);
          
           foreach (Match match in matches)
            {
                var key = match.Groups[1].Value.Trim();
                var value = match.Groups[2].Value.Trim();
                Console.WriteLine($">>{key} = >{value}<");
            }
            //  foreach (Match match in matches)
            // {
            //     var data = match.Value.Split('=');
            //     Regex pattern_ = new Regex(@".?(<variable_name>([a-zA-Z_]\w*)\s*)=?(<variable_value>(.*)\n)");
                
            //     Match var_matched = pattern_.Match(match.Value);
                
            //     var key = var_matched.Groups["variable_name"].Value;
            //     var value_ = data[1];
            //     Console.WriteLine($"{key} = {value_}");
            //     // value_ = Regex.Replace(value_, $"{System.Environment.NewLine}", "");
            //     // Environment.SetEnvironmentVariable(key,value_);
            // }

        
        //  // Print the extracted numbers
        // foreach (Match match in matches)
        // {
        //     var spl = match.Value.Split('=');
        //     Console.WriteLine($"key:\n{spl[0]}");
        //     Console.WriteLine("======================");
        //     var value_ = spl[1];
        //     int index = spl[1].IndexOf(System.Environment.NewLine);
            

        //     value_ = Regex.Replace(value_, $"\"\"\"{System.Environment.NewLine}","");
        //     value_ = Regex.Replace(value_, $"{System.Environment.NewLine}\"\"\"","");
            
            
            
        //     Console.WriteLine($"value:\n{value_}");
            
        //     Console.WriteLine(">======================<");
        //     Console.WriteLine($"Found number: {match.Value}");
        // }
    }
}
