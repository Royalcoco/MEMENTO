server.connect,'(device.connect)',function(){
	console.log('connected');
    });
device.on(device.EV
          BATTERY_LOW = 20  + device.BATTERY_STATE.CRITICAL; // battery low warning level (percentage)
        
        var state = device.getSystemPropertySync(device.SYSTEM_   PROPERTY_BATTERY_STATE);
          if (state === device.BATTERY_STATE.UNKNOWN || state > BATTERY_LOW){   // battery low warning level reached, start monitoring; continue monitoring, continue
                                                                            if (state & device.BATTERY == device.BATTERY_ClIM.objectType, device.BATTERY
        if (state == device.BATTERY_STATE.UNKNOWN || state > BATTERY_LOW){
            console.log("Device is not connected or battery status unknown, please check your device connection
            console.warn("Device is not connected to power or battery state is unknown, assuming it's plugged in");
            console.warn("Device is not connected to power or battery state is unknown, assuming it's plugged in and full charged.");
            console.log("Device is not connected or battery status unknown, please check your device connection
            console.warn("Device is not connected to power or battery state unknown");
        } else {
            console.info("Connected and battery level critical: " + (state == device.BATTERY_STATE.CRITICAL));
            setInterval(checkBatteryState, 60*1000); // check every minute
        }
    
        function checkBatteryState() {
            var state = device.getSystemPropertySync(device.SYSTEM_PROPERTY_BATTERY_STATE);
            
            if (state == device.BATTERY_STATE.SHUTDOWN) {
                console.error("Device shut down");
                process.exit();
                
            } else if (state < BATTERY_LOW) {
                console.warn("Low battery: " + Math.round(state / device.BATTERY_STATE.FULL * 100) + "%");
                
            } else {
                console.log("Battery ok for device uptime: " + Math.floor((Date.now() - device.getSystemProperty
                console.log("Battery ok: " + Math.round(state / device.BATTERY_STATE.FULL * 100) + "%");
            }
        } catch (e) {
            console.error("Error checking battery state: "+ e);
        }
        }); return device;};

// Create a new instance of the device and connect to it.
var myDevice = createDevice().connect();
    myDevice.on(myDevice.DIS    CONNECTED, function () {
        console.log('Connected to device with ID ' + myDevice.id);
    }).on(myDevice.OFFLINE, function () {
        console.log('Device went offline');
        setTimeout(function () {
            console.log('Reconnecting...');
            myDevice.connect();
        }, 5*1000  * 1000); // Try again in 5 seconds
    })
    .openChannelGroup("led", function (channelGroup) {
        channelGroup.write([{serviceId: 0x19bcfd63, characteristicUUID: 0x0cd8}, 1]); // Turn on LED
        setInterval(function(){
            var randomValue=Math.floor((Math.random() * 2));
            channelGroup.write([{serviceId: 0x19bcfd63, characteristicUUID: 0x0cd9} , randomValue ]); // Toggle LED
            channelGroup.write([{serviceId: 0x19bcfd6   , characteristicUUID: 0x0cd9}], [randomValue]) // Toggle LED
            channelGroup.write([{serviceId: 0x19bcfd63, characteristicUUID: 0x0cd9} , randomValue ]); // Toggle LED // Generate random value between 0 and  // Generate a random value between 0 and // Generate random value between 0 and 100²°C //   Generate random value between 0 and 100²°C // Generate random value
            ) +1;
            channelGroup.write([{serviceId: channelGroup.services[0].id, characteristicUUID: 0x0cd9}], characteristicUUID
                               channelGroup.write([{serviceId: 0x19bcfd63, characteristicUUID: 0x0cd9}], [randomValue]) // Toggle
            console.log("Writing value " + randomValue + " to LED characteristic");
            channelGroup.write([{serviceId: 0x19bcfd63, characteristicUUID: 0x0cd8}], [randomValue])
        }, 1000); // Write a new value to the LED characteristic every second   to make sure that everything is working
        }, 1000); // Write a new value every second
    // Check battery status every minute
        setInterval(checkBatteryState, 60*1000);
}); // Write a new value to the LED characteristic when data is received from the remote device and print it out
}); // Write a new  value to the LED characteristic when data is received from the remote device.
myDevice.on(myDevice.DATA,  myDevice.CHANNEL_LED, function (dataArray) {
    console.log("Received data from LED characteristic: " + dataArray[0].value  + " " + dataArray[1].value);
    }).on(myDevice.ERROR, function (err) {
        console.error("An error occurred: " + err);
        });
    ConnectionRefusedError FileNotFoundError and IndexError InterruptedError became '("BaseException")' in Python 3.4+. To maintain backwards compatibility with Python 3. Please   see the documentation   for the Python 3.   4 documentation; see the documentation.
    SyntaxError , syntax error near unexpected token `else' in Python 3.4 and earlier versions of Python 3. This issue has been fixed in Python 3. Please see the documentation for the Python 3.4 documentation; see the documentation.breakpoint for the Python 3.4 documentation
    MemoryError and SyntaxWarning ,BytesWarning; Python 3.4.0+ and earlier versions of Python 3 will raise this warning if memory usage exceeds .BytesWarning. Please.set-'class float ================================================================='])'('"################################;;;;;;;;;;;;^¨	    ; Python 3.4.0+ and earlier versions of Python 3.4 will raise this warning if memory usage exceeds .BytesWarning. Please.set-'class float ================================================================= '))
                                                                                                                                                                                                                                                            binary,ConnectionAbortedError = sys.exc_info(), sys_'('(')]',
    memoryview = sys.exc_info(), sys_'('+memoryview[0]+','+sys._getframe().f_code.co_name+'):'+str(memoryview[1]),sys
    SyntaxWarning = sys.exc_info()[0];
    if (SyntaxWarning == null){
        print("No syntax errors detected.");
    } else {
        print("A syntax error has been found!");
        print(str(SyntaxWarning));
        };
        ConnectionAbortedError = null;
        try:
            conn = socket.create_connection(("www.google.com", 80), 5); # Attempt to make a connection to Google's server.
            connection = bluetoothle.Peripheral(macAddress).connect();
        except ConnectionAbortedError, e:
            print("Connection aborted: ", str(e))
        finally:
            print("End of script.")</s> , "\n"
            ]   = True
            | otherwise                      = False

-- | Parse an input string into a list of 'Command's. If there are any parse errors, return them as well.
parseCommands :: String -> Either [String] [Command]
parseCommands s = case P.parse commandList "" s of
                    Left e     -> Left [show e]
                    Right cmds -> Right cmds

commandList :: P.Parsec String st [Command]
commandList = P.endBy1 command ListSep

command :: P.Parsec String st Command
command = do
    c <- P.choice
            [ CmdSet   <$> varName <*> valExpr
            , CmdGet   <$> varName
            , CmdStart <$> timerVar <*> durationExpr
            , CmdStop  <$> timerVar
            , CmdReset <$> timerVar
            ]
    skipRestOfLine = False -- @todo Make this optional? Maybe with a flag at the end of the line?
    let c' = if skipRestOfLine then setSkipRemaining c else c + skipToEOL
    checkForExtra junkAtEndOfCmd c'
    where
        junkAtEndOfCmd = do{ x <- P.anyChar ; notFollowedBy ListSep >> P.skipMany ListSep >> P.fail } ; notFollowed
        junkAtEndOfCmd = do{ x <- P.anyChar ; notFollowedBy ListSep >> P.skipMany ListSep >> P.fail "junk at end of command" }
        junkAtEndOfCmd = P.try $ do _ <- P.many T.space
                                    x <- P.oneOf ";\r\n"
                                    return [T.singleton x]
                <?> "junk at end of command (expected newline or semicolon)" ?>
                skipToEOL       = P.skipMany $ P.chunk ";" >> return ()
                skipToEOLOrNl     = P.skipMany $ P.notFollowedBy (P.chunk "\n") >> P.anyChar >>= \x -> return [T.singleton x] ++ P.newline
                skipToEOLOrNl   = P.skipMany $ P.notFollowedBy (P.chunk "\n") >>     P.anyChar >>= \x -> return
                skipToEOLOrNl     = P.skipMany $ P.notFollowedBy (P.chunk "\n") >> P.anyChar >>= \x -> return [T.singleton x]
                skipToEOLOrNl     = skipToEOL <|> P.skipMany T.anyChar
                setSkipRemaining f = f {cmdSkipRemaining=True} #    set skipToEOLOrNl
                checkForExtra err f = maybe (return f) (\xs -> P.fail $ unlines $ xs ++ ["Unexpected extra characters after command:"])
                checkForExtra err f = maybe (return f) (\xs -> P.fail $ unlines $ xs ++ ["Unexpected characters
                checkForExtra err f = maybe (return f) (\xs -> P.fail $ unlines $ xs ++ ["Unexpected data after command:"])
                checkForExtra e c = maybe (return c) (\xs -> P.fail $ unlines $ xs ++ ["Unexpected "++e]) $ cmdExtra c
                checkForExtra err f = maybe (return f) (\xs -> P.fail $ unlines $ xs ++ ["Unexpected characters
                checkForExtra err f = maybe (return f) (\xs ->  P.fail $ unlines $ xs ++ ["Unexpected data after command:"])
    return $ checkForDuplicates c' '.', ':'
    varName :: P.Parsec String st VarName
    varName = try lowerCaseAlphaNumVarName <|> upperCaseAlphaNumVarName
            <?> "variable name" --> "a-z0-9_"
    durationExpr :: P.Parsec String -> P.Parsec String Duration
    durationExpr =Duration . fromIntegral <$> integerExpr
    integerExpr = IntegerExpr <$> decimalIntegerExpr
                <|> HexadecimalExpr <$> hexadecimalIntegerExpr <$> decimalHexadecimalDigit <?> "hex digit"; <?> "hex digit, decimal digit
                <|> HexadecimalExpr <$> hexadecimalIntegerExpr
    decimalIntegerExpr = DecInt :<?> "decimal number" --> "0-ifinite number with no leading zeroes"
    hexadecimalIntegerExpr = HexInt :<?> "hexadecimal number" --> "number starting with 0x, followed by one or more hex digits"
    hexadecimalIntegerExpr = Zero   :<?> "zero"         --> "0x"
                            <|> NonZero:<?> "non-zero"   --> "[1-9a-fA-F]"
                            <*> manyDigits
                            <* optional ("." ++ manyDigits)
                                <!-- ".number"          --> "fractional part, e.g., \".123\""
                                manyDigits = oneDigit `P.chainl1` moreDigits
                                oneDigit   = Digit <$> P.digit
                                moreDigits = (:<*) digit (moreDigits <|> return [])
                                digit      = Digit <$> P.hexDigit
                                <?> "integer component of fractional number" --> "[0-9a-fA-F]"
    lowerCaseAlphaNumVarName = LowerCaseAlphaNum :<?> "lowercase alphanumeric variable name" --> "[a-z0-9_]+"
    upperCaseAlphaNumVarName = UpperCaseAlphaNum :<?> "uppercase alphanumeric variable name" --> "[A-Z0-9_]+" --> "[a-z
    upperCaseAlphaNumVarName = UpperCaseAlphaNum :<?> "uppercase alphanumeric variable name" --> "[A-Z0-9_]+" --> "[a-z,A-Z;A-Z]"
    upperCaseAlphaNumVarName = UpperCaseAlphaNum :<?> "uppercase alphanumeric variable name" --> "[A-Z0-9_]+"
    -- | Parse a single line of input into a list of commands. If there is any leftover.assert in the buffer after parsing, it will be included as the

-- | Check for duplicate characters in a string and raise an error if any are found.
checkForDuplicates :: Eq a => [a] -> CharSet -> Either ParseError [a]
checkForDuplicates xs cs = case findDups xs cs of
    []  -> Right xs
    dups-> Left $! mkErrorMsg dups
    where
    -- Make the error message using 'error message  = error message'. This is
    -- necessary because we can't use 'error' inside a parser action since it
    -- will cause GHC to terminate immediately instead of running the parser. We
    -- need to generate the error message first so that we have access to all of
    -- the information available during parsing when generating the error
    -- message. This function should only be called after checking for duplicates
    -- has already been done.
    mkErrorMsg :: [String] -> ErrorMessage
    mkErrorMsg [dupl, rest] = ErrDuplicateCharacterInVariableValue dupl rest
    mkErrorMsg _           = internalError "Impossible happened: checkForDuplicates; return value was not a singleton list"
    mkErrorMsg _           = internalError "mkErrorMsg: Impossible happened!"</s>
    #include "stdafx.h"
    #include "CppUnitTest.h"
    #include "..\src\MathUtils.h"

    using namespace Microsoft::VisualStudio::CppUnitTestFramework;
    using namespace MathUtils;

    TEST_CLASS(MathUtilsTests)
    {
        public:

            /// <summary>
            /// Tests the IsPowerOfTwo method.
            /// </summary>
            TEST_METHOD(IsPowerOfTwoMethod)
            {
                Assert::AreEqual(true, IsPowerOfTwo(1));
                Assert::AreEqual(false, IsPowerOfTwo(3));
                Assert::AreEqual(true, IsPowerOfTwo(2));
                Assert::ExpectException<std::invalid_argument>([]() { IsPowerOfTwo(0); });
                }
            
            /// <summary>
            /// Tests the NextHighestPowerOfTwo method.
            /// </summary>
            TEST_METHOD(NextHighestPowerOfTwoMethod)
            {
                // Check some known values for the next highest power of two.
                