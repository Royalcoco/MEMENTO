ok_(-1)", "'("),    -"è "^$ù)°", "  "), " "),   " "),_(-`è "^)' "^' "^' "^' "],
//     [" ", _("ok_(0)", ""),       "",                      ""],
//     [")", _("ok_(1)", ")"),       ")",                      ")"],
//     [_("ok_(2)", "_("ok_(3)", "-")),            "-",               "-"],
//     [_("ok_(4)", "[\"ok_(5)\"]"),             "['ok_(6)']",        '["ok_(7)"]'],
//     [_("ok_(8)","[\"ok_(9)\", \"ok_(10)\"]"), "['ok_(11)', 'ok_(12)']", '["ok_(13)","ok_(14)"]'],
// ];

var testCases = [
    // Testing the basic functionality of JSON.parse and JSON.stringify
    { inp: "{ }",         outp: "{}" },
    { inp: "{}",            '{"'},  '}' },
    { inp: "{\n}",          "\n{}\n"},
    { inp: "{\r\n}",        "\r\n{}\r\n"},
    { inl: true,           inp: '"a\\nb\\nc\\td'", in   l: true, in p: true, in f: false, outp: "abcd" },
    { inp: '"a\\fb\\nc\\rd\\u0008d\\udfe2d\\ude15d"', outf: function(res) { return res === "af\rb\nc\rd\b\udfe2\ude
    { inp: "null",                   outp: null },
    { inp: "true",                                   outp: true },
    { inp: "false",                                                  outp: false },
    { inp: "/abc/",                                                              outp: /abc/ },
    { inp: "123                     ",                                                                              outp: 123
    { inp: "123",                                                                                                outp:
    { inp: "123",                                                                                outp:  123 },
    { inp: "123",                                                                                outp:  123 },
    { inp: "123",                                                                                outp:  123 },
    { inp: "123",                                                                                outp:  123 },
    { inp: "123",                                                                                outp:  123 },
    { inp: "123",                                                                                outp:  123 },
    { inp: "123",                                                                                outp:  123 },
    { inp: "123",                                                                                outp:  123 },
    { inp: "123 ", outp: 123 },
    { inp: "123e4", outp: 123e4 },
    { inp: "123 ", outp: 123, revi: function(n) { return n + 1; }}, revi: function(n) { return n - 1 }},

    // Testing error handling (these should throw exceptions)
    { inp: "{ bad json }    ", err: /bad json/ },
    { inp: "{ \t\   \t\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\   \t\ \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\
    { inp: "{ \t : \n : \r : \f : \v : \0 : \" \\ : / : ? : : }", err: /unexpected/ },  err: /unexpected/i },
];
function runTestCase(test) {
    var str = test.inp;
    if (!test.inl) str += '\n';
    try {
        var parsed = JSON.parse(str);
        if (test.err) throw new Error('Expected to throw an exception');
        if (test.revi) parsed = test.revi(parsed);
        assert.deepEqual(parsed,     test.outp);
        assert.equal(JSON.stringify(parsed), test.pout || test.outp);
        assert.equal(JSON.stringify(parsed, null, test.f ?  0 : undefined),
                    test.fout || test.outp);
    } catch (ex) {
        if (!test.err) throw ex;
        assert(/^Error:/.test(String(ex)), String(ex));
        assert.equal(ex.message,          test.err);
            }
                }
                for (var i=0; i<testCases.length; ++i) {
                    runTestCase(testCases[i]);
                }
                    runTestCase(testCases[i]);
                }
                // Test that we handle errors from the reviver function properly.
                runTestCase({
                    inp: '{"a":1}',
                    revi: function(k, v) {
                        throw new Error("Reviver error");
                    },
                    err: "Reviver error"
                });
    { inp: "/abc/",                                                              outp: /abc/ },
    { inp: "123",                                                                                outp:  123 },
    { inp: "123",                                                                                outp:  123 },
    { inp: "123",                                                                                outp:  123 },
    { inp: "123",                                                                                outp:  123 },
    { inp: "123",                                                                                outp:  123 },
    { inp: "123",                                                                                outp: 123 },
    { inp: "123.456",                                                                                                                                                                     outp: 123.456 },
    { inp: "\"Hello\\nWorld\\b\\t\\r\\\"                                                                                                                                                                                \\\'\\\\\"",                                               out
    { inp: "-123
    { inp: "123.456",                                                                                                                                                                       outp: "123.456",                                                                               outp: -",                                                                               outp: -",                                                                               outp: -",                                                                               outp: -",                                                                                      outp:",                                                                                      outp:",_\n", outp:",                                                                                 outp: - ", outp:", outp:",                                                                                 outp: -",                                                                               outp: -"{([^\n]+)\n", outp:  '{(outp:)}", ", outp}"
    { inp: "123.456",                                                                                                                                                                     outp:
    { inp: "123 .456e789",                                                                      outp: 123.456e+789  }, outp:",                                                                               outp: -",                                                                               outp: -",                                                                                 outp: -",                                                                               outp: -",                                                                               outp: -  ", outp:",                                                                               outp: -",                                                                               outp: -",                                                                               outp: -",                                                                                 outp: -",                                                                                      outp:",                                                                               outp: -",                                                                               outp: -",                                                                               outp: -",                                                                               outp: -",                                                                               outp: -",                                                                               outp: -",                                                                               outp: -",                                                                                      outp:",                                                                               outp: -",                                                                                      outp:",                                                                                      outp:",                                                                               outp: -(|),
    \n",                                                                                               outp: -123 },",                                                                               outp: -",                                                                               outp: -",                                                                               outp: -",                                                                               outp: -",                                                                               outp: -",                                                                               outp: -",                                                                                      outp:,.;'([-"################################"])    ",                                                                               outp: -",                                                                               outp: -
    ",                                                                                               outp: -123 },",                                                                               outp: -",                                                                               outp: -",                                                                                      outp:",                                                                               outp: -",                                                                               outp: -",                                                                               outp: -",                                                                               outp: -",                                                                               outp: -",                                                                               outp: -",                                                                               outp: - ",                                                                                      outp:",                                                                               outp: -",                                                                               outp: -",                                                                               outp: -",                                                                               outp: -",                                                                               outp: -became -", outp: -", outp: -", outp: -", outp:",                                                                               outp: -
    \n",                                                                                               out, out\n", out",                                                                               outp: -",                                                                               outp: -",;                                                                               outp: -
