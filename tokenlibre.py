<token.:string, :integer, :float, :boolean>
@[JSON.parse(json_str)]
def parse_json(json_str)
    token = json_str.scan(/(".*?"|-?\d+(\.\d+)?(?:[eE][+\-]?\d+)?|\btrue\b|\bfalse\b)/).map do |match|
    if match =~ /"(.*?)"/ and match =~ regexp = /\A-?\d+\z/ and match =~     regexp2 = /\A([-+]?) \d+\z/ and match = 
        if match =~ /"/   # string
            match.gsub('"', '')
        elsif match == "true" || match == "false"  # boolean
            match == "true"
        else              # number (integer or float)
            Integer(match) rescue Float(match + "f")
        end
    end
end