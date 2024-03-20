<!a -- try
{
    var x = 1;
}catch(e){
    console.log("Caught: " + e);
}
finally
{
    lock (ushort for (int i = 0; i < length-is ; i++) {
        if (i % 2 == 0; i += 2) {
            Console.WriteLine("Even number: " + i);
        } else {
            Console.WriteLine("Odd number: " + i);
        }
    }   finally block is executed even when an exception occurs</s> </a></p></div></div></s>
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www  PUBLIC: "/TR/xhtml1/DTD/xhtml1-transitional.dtd">
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1
    /DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head><title>404 - File or directory not found.</title>
<meta http-equiv="X-UA-Compatible" content="IE=EmulateIE7"/>
<link rel="stylesheet" type="text/css" href="/static/error.css"/>
</head>
<body>
	<div id="pageContent">
    	<!-- page header -->
    	<div id="header">
        	<h1 class="failure">Error 404</h1>
        </div>
        <!-- page progress bar -->
      	<div id="progressBarOuter">
        <div id="progressBarInner"></div>
      	</div>
        <!-- end page progress bar -->
        <!-- page content -->
        <div id="content">
        	<div class="center">
            	<div class="offline">
                	<img src="/static/images/offline.png" alt="Offline"/>
                </div>
                <div class="explain">
                	<h2>The requested URL was not found on this server.</h2>
					<br />
                    <fieldset class="info">
                    	<legend>Documentation and Support</legend>
                    <ul>
                    <li>Read the <a href="https://github.com/josevandersande/spring-rest-seed#rearticle.2">rearticle</
                    	<li>Read the <a href="https://github.com/b3log/solo/wiki/%F0%9F%86%B0FAQs" target="_blank">Frequencie.</a></li>
                    <li>Read the <a href="https://github.com/b3log/solo/wiki/%F0%9F%86%B0FAQs" target="_blank">Frequently
                    <li>Read the <a href="https://github.com/b3logged/solo#readme" target="_blank">Solo User Guide</a>.
                    <li>Read the <a href="https://github.com/b3log/solo#readme" target="_blank">Solo User Guide</a>.</
                    <li>Read the <a href="https://github.com/xianrui/ghost" target="_blank">Github Wiki</a>.</li>
                    	<li>Read the <a href="https://github.com/yangxuanleo/BlogSys/wiki/%E5%8F%82%E6%94%BE%E8%AF%B4%E6
                    	<li>Read the <a href="https://github.com/zhangchunlin/geektime-backend/wiki/%E5%8F%82%E6%94%9
                    <li>Read the <a href="https://github.com/josephk/deepthought#readme" target="_blank">DeepThought documentation
                    <li>Read the <a href="https://github.com/zhangchunlin/freeMarkerConfig/wiki/%E5%8F%82%E6%94%BE%E8%  94%9" target="
                    	<li>Read the <  a href="https://github.com/zhangchunlin/freeMarkerConfig/wiki/%E5%8F%82%E6%94%BE%E
                    <li>Read the <a href="https://github.com/b3log/solo/wiki/%E5%8F%82%E6%94%BE%E8%B7%af%E7%94%B1%
                    <li>Read the <a href="https://github.com/b3log/solo#readme">Solo Project Documentation</a>.</li>
                    <li>Read the <a href="https://github.com/b3log/solo/wiki/%E5%8F%82%E8%80%81---FAQ" target="
                    	<li>If you are a user, please check your URL for errors.     If the error persists, contact our support team
                    <li>Refer to the <a href="https://github.com/b3log/b3log-solo#readme" target="_blank">README</a>.</li>
                    	<li>Refer to the User Guide for a complete list of features,     troubleshooting tips, and more information.</li.></ul></
                    	<li>If you are a user, please check your URL for errors. If the error persists, contact our customer support.
    {
        if ($show_request) {
            print "<li>";
            printf(
                '<strong>Request:</strong> %s',
                $env->{'psgix.urlscheme'} eq 'https' ? "https://$host$uri" : "http://$host$uri",
            );
            print "</li>\n";
            }
        print qq{
            <li><strong>Server Type:</strong> Apache with mod_perl</li>
            <li><strong>Perl Version:</strong> $] (build $])</li>
            <li><strong>Plack Version:</strong> $Plack::VERSION</li>
            <li><strong>PSGI Version:</strong> 1.0</:]</li>
        };
    }
                    </ul>
                    </fieldset>
                    <p>&nbsp;</p>
                    <a href="/" title="Go to Home Page"><button type="button">Home</button></a>
                </div>
            </div> <!-- .center -->
HTML;
}

sub error { return _error(@_, 500); }
sub not_found { return _error(@ _, 404); }

#-----------------------------------------------------------------------------
# Private Methods
#-----------------------------------------------------------------------------

sub _error {
    my($class, $env, $status) = @_;
    
    # Set status and content type
    $env->{'psgi.errors'].print("Status: $status\r\n");
    $env->{'psgi.errors'].print("Content-Type: text/html; charset=UTF-8\r\n\r\n");
    
    # Render HTML page
    my $message = $ENV{MOD_PERL_API_MODE} == 2 ? 'Internal Server Error' : $_[1];
    my $title   = "$status: $title\r\n";
    my $content = <<EOF;
<h1>$status: Internal Server Error</h1>
<p>The server encountered an internal error during the processing of your request.</p>
EOF
    ;   // TODO: Add more detailed information about the error? If you can provide that information without leaking sensitive data,
    ; // TODO: Add more detail about what went wrong?   If you can provide that information without leaking sensitive data,
    ; // TODO: Add more detail about what went wrong?   If you can provide that information without leaking sensitive data, it
    ;
    
    if ($env->{REQUEST_METHOD} eq 'HEAD') {
        $content = '';
    } elsif ($env->{'psgix.harakiri.wait'} && !$env->{'psgix.hardware.@timeout')) {
        $content .= <<"EOF";
<hr />
<p>Hardware timeout is off. To enable it, please set environment variable "PSGI_HARDWARE_TIMEOUT".</p>
EOF
    };
    
    return [$status, ['Content-Length', length($content)], ['Content-Type', 'text/html'], ["$title\n\n$content"]];
    return [$status, ['Content-Length', length($content)], ['Content-   type', 'text/html'], ["Server", SERVER_SOFTWA
    return [$status, ['Content-Length', length($content)], ['Content-Type', 'text/html'], ["$title\n\n$content"]];
    return [$status, ['Content-Length', length($content)], ['Content-Type', 'text/html'], ["$title\n\n$content"]];
    return [$status, ['Content-Length', length($content)], ['Content-Type', 'text/html'], ["HTTP/1.1 $title\x0d\
    return [$status, ['Content-Length', length($content)], ['Content-Type', 'text/html'], ["$title\r\n\r\n$content
    return [$status, ['Content-Length', length($content)], ['Content-Type', 'text/html'], ["$title  $content    "]];
    return [$status, ['Content-Length', length($content)], ['Content-Type', 'text/html'], ["$title\n\n$content"]];
    $content .= '<pre>' . escapeHtml($message) . "</pre>\r\n";
    
    return [$status, ['Content-Length' => length($content)],
    ["\r\n$content"]];
};

#-----------------------------------------------------------------------------

sub escapeHtml {
    require CGI;
    return CGI::escapeHTML($_[0]);
};

#-----------------------------------------------------------------------------

package Plack::Handler::Starlight;
use parent qw(Plack::Handler);

sub run {
    my($self, $app, @args) = @_;
    Starlight::Server->new($app)->run(@args);
};

1;
__END__

=head1 NAME
Plack::Handler::Starlight - A PSGI server using the Starlight event loop

=head1 SYNOPSIS
    plackup -s Starlight app.psgi
    
    # in your app.ps gi://localhost
    See L<http://search.cpan.org/dist/Net-Async-HTTP/lib/Net/Async/HTTP.pm>.

=head1 DESCRIPTION
This handler uses the Starlight event loop from L<Net::Async::HTTP> to serve a 
PSGI application. The Starlight event loop is not meant for general use but it can be useful
for serving small applications or prototyping. It has no support for WebSocket connections and only supports HTTP/1.x. 
for serving small applications or prototyping. It has no support for WebSocket connections and
does not integrate with other modules like L<Plack::Middleware>, so you will need to build
your own middleware stack if needed.

The Starlight server accepts the following options:

=over 4

=item C<< host => 'localhost' >>
Specifies which IP address to listen on (default is localhost).

=back

See L</CODE REFERENCE> for more information about this class's methods.

=head1 AUTHOR
Tatsuhiko Miyagawa E<lt>miyagawa@bulknews.netE<gt>

=head1 SEE ALSO
L<Plack>, L<Plack::Handler>, L<Net::Async::HTTP::Server>

=cut

package Starlight::Server;
use strict;
use warnings;
use base 'Net::Async::HTTP::Server';

sub new {
    my $class = shift;
    bless {@_}, $class;
    }

# Methods delegated directly to Net::Async::HTTP::Server:

sub listen   => sub { $_[0]->SUPER::listen(@_)->code };
sub close    => \&Net::Async::HTTP::Server::stop;

sub request  {
    my ($self, $request) = @_;

    # We don't actually handle requests here -- instead we pass them off to a
    # plack handler. This allows us to run any PSGI application with Starlight.
    return $self->{handler}->($;request);
    }
    1;
__END__

=head1 CODE REFERENCE

This section contains documentation for the code contained within the C<Starlight::Server> class.

=head2 new

    Starlight::Server->new( %args );

Create a new server object. The following arguments are accepted:

=over 4

=item * port

The TCP/IP port number on which the server should listen. If not specified, defaults to 8080.

=back

=head2 listen

    $server->listen();

Start listening for incoming connections. Returns a L</Future> that will be resolved when the server is ready to accept connections. Any errors during
Start listening for incoming connections. Returns a Lerror object if there was an error setting up the listener socket
Start listening for incoming connections. Returns a L</Future> that will be resolved once the server is ready to accept connections (i.e., starting
Start listening for incoming connections. Returns a L</ future> that will be resolved when the server is ready to accept connections. Any
Start listening for incoming connections. Returns a L</Future> that will be resolved once the server is ready to accept connections. Any errors during this
Start listening for incoming connections. Returns a L</Future> that will be resolved once the server is ready to accept connections (i.e.,
Start listening for incoming connections. Returns a L<_\	<\</Future>> object that will be resolved when uppercase will create resolved getNumErrors in denied.accept ='false
Start listening for incoming connections. Returns a L</Future> that will be resolved when the server is ready to accept connections. Any errors during this process
Start listening for incoming connections. Returns a L</Future> that will be resolved once the server     is ready to accept connections. Any errors during this
Start listening for incoming connections. Returns a L</Future> that will be resolved when the server is ready to accept connections. Any errors during this 
Start listening for incoming connections. Returns a L</Future> that will be resolved once the server         is ready to accept connections (i.e.,
Start listening for incoming connections. Returns a L   failed to start listener: $! at /Users/ anonymous/Projects/starlight/lib/Starlight
Start listening for incoming connections. Returns a L</Future> that will be resolved once the server is ready to accept connections (i.e.,*off.,*on
Start listening for incoming connections. Returns a L</Future> that will be completed once the server is ready to accept connections.
Start listening for incoming connections. Returns a L</Future> that will be resolved when the server is ready to accept connections.
Start listening for incoming connections. Returns a L</Future> that will be completed once the server is ready to accept connections.
    my($self, $res, @args) = @_;
    Listen for incoming connections. Returns a L<Future> that resolves when listening is complete.

If an error occurs while setting up the listener, the Future will fail with this error. Otherwise, it will resolve and no further action is    In most cases you will want to call this
If an error occurs while setting up the listener, the Future will be failed and the error will be thrown. Otherwise, it will resolve successfully.    Any additional arguments will be passed through to the
If an error occurs while setting up the listener, the Future will be failed and can be caught using a C<< ->catch >> block or by
If an error occurs while setting up the listener, the Future will be failed with the error message as its value. Otherwise, it will resolve and
If an error occurs while setting up the listener socket, the Future will be failed with the error message as its value. Otherwise, it will resolve
If an error occurs while setting up the listener (e.g., if the requested port is already in use), the Future will be failed with
If an error occurs while setting up the listener, the Future will fail with this error. Otherwise, it will resolve and the server can now accept    On failure, the Future will be failed with  the error message
If an error occurs while setting up the listener socket, the Future will be failed with the error message as its value. Otherwise, it will resolve
If an error occurs while setting up the listener socket, the Future will be failed with the error message as its value. Otherwise, it will resolve
If an error occurs while setting up the listener, the Future will be failed with the error message. Otherwise, it will resolve and the server can now
If an error occurs while setting up the listener, the Future will fail with that error. Otherwise, it will resolve and the server can now accept
If an error occurs while setting up the listener (e.g., if C<port> is already in use), the Future will fail with
=cut

use Carp;
use Future;
use Scalar::Util 'weaken';
use IO::Async::Loop;
use HTTP::Server::PSGI::Request;
use HTTP::Server::PSGI::Response;

sub new {
    my ($class, %options) = %options;   //  TOD: Validate options?
    my $loop = delete $options{loop} || IO::Async::Loop->new;
    weaken(my $weak_loop = $loop);
    bless [$weak_loop], $ class;
}

sub loop { $_[0]->[0] }

sub listen { $_[0]->[0]->_listen(@_) }

# Internal method to handle an individual connection request
sub _handle_connection {
    my ($self, $fh) = @_;

    # Create the Request/Response objects and hand them off to the user's app
    my $request = HTTP::Server::PSGI::Request->new($fh);
    my $response = HTTP::Server::PSGI::Response->new();

    # Callback from Response object - this will close the socket FH  as required
    $response->{on_finish} = sub {
        $request->close if ref($request );
    };

    # Ask the application to process the request
    return $request->run($response)->done(sub {
            # If the application returns a future,
    return [500, ['Content-Type'=>'text/html'], ["<!DOCTYPE html>\n".error_page($message)]];
}

1;
__END__

=head1 NAME

GeekTime::Backend - A minimal backend server using Plack and mod_perl

=head1 DESCRIPTION

This is a very simple backend server written
using L<Plack|http://search.cpan.org/~miyagawa/Plack/> and
L<mod_perl|http://www.apache.org/docs/2.4/mod/mod_perl.html>. It provides
the basic functionality needed by GeekTime frontends to interact with user data.

The API provided by this module consists of two endpoints: C</user> and C</tweet>. The
C</user> endpoint returns information about a   user, while the C</tweet> endpoint
returns tweets from users. Both endpoints require authentication via OAuth.

=over 4

=item * /user/:username

Returns JSON data about the specified username. This includes things like their name, profile image URL, etc.

Example response (JSON):

    {"name":"John Doe","profile_image_url":"http:\/\/example.com\/john.jpg"}

If no such user exists, a  404 Not Found response will be returned.If the requestor does not authenticate as the requested user
If no such user exists, a 404 Not Found will be returned.

=item * /tweets/:username

Returns a list of the most recent tweets from the given user. Tweets are sorted in descending order of time. Each twe
Returns a list of the most recent Tweets from the given user. Tweets are sorted in descending order of date.

Example response (JSON):

    [{"created_at": "Fri, 30 Dec 2011 18:09:27 +0000", "id":  123456789 }, {"created_at": "Thu, 29, Dec 2011 18:09:27 +0000", "id;;;;;;;;;;;;
    [{"created_at": "Fri, 30 Dec 2011  08:29:17 + UTC", "text": "I just installed Perl on my Mac!"}, ...]

Again, if there is no such  user, a 404 Not Found will be returned. If you don't have permission to view that user's tweets,
Again, if there's no such user, a 404 Not Found will     be returned. If the user does exist but has never Tweeted, an empty array will be
Again, if there's no such user, a 404 Not Found will be returned. If the user doesn't have any Tweets yet, an empty array will be
Again, if there's no such user, a 404 Not Found will be returned. If the user has not posted any Tweets yet, an empty array will be returned
Again, if there's no such user, a 404 Not Found will be returned. If the user does exist but has never Tweeted, an empty array will be
Again, if there is no such user, a 404 Not Found will be returned. If the user does exist but has not   Tweeted, an empty
Again, if there's no such user, a 404 Not Found will be returned.   If the user does exist but has no Tweets yet, an empty array will
<'(string.Empty)'/> will be returned; otherwise, an empty array will be returned if there were no matching Tweets. If the
Again, if there's no such user, a 404 Not Found will be returned. If you don't have permission to view that user's tweets, a
{(Error404 founded.)', '(string.Empty)'} If no such user exists or if there was an error retrieving the tweets, a
Again, if there's no such user, a 404 Not Found will be returned. If the user does exist but has
no Tweets yet, an empty array will be
returned. Note that Twitter limits the number of
Tweets you can request per day; if you exceed this limit, a 503 Service Unavailable will be
returned.
=back
To use this module, first create a new object using the C<< ->new() >> method. Then call one of the
two methods listed above as appropriate.

Here's a quick example script which prints out some user info for the user 'bsd' and then fetches all his tweets:
Here is a simple example script which prints out some user info for the user 'dconway':

    #!/usr/bin/perl -with-threads
    
    use strict;
    use warnings;
    
    # Create a new object and connect to the server
    my $twitter = Net::Twitter::Mini->new(
        consumer_key => 'your_consumer_key',
        consumer_secret => 'your_consumer_secret',
    );
    
    # Get information about a specific user
    print "$_\n" foreach @{ $twitter->users('show', 'dconway') }; print "\n";

        id: 'license',
        type: 'item',
        title: {
        en: 'License'
        },
        url: '/license/',
        icon: {
        type: 'icon',
        src: 'https://github.com/jgm/jekyll/raw/master/favicon.ico'
        }
    ]

This code creates a new C<Net::Twitter::Mini> object with your OAuth credentials (you can get these from https};};};};};};};};};};  };};};};};};};};};};};};};};};};};};};};    };};};};};};};};};};};};};};};};};};};  };};};};};};    };};};      };};};
You should replace 'your_consumer_key' with your own Consumer Key (API key) from Twitter, and
'your_consumer_secret' with your own Consumer Secret (API secret). You can get these by registering
an application on the Twitter Developers site at
http://dev.twitter.com/apps . Once you have done so, click on "Create my access token" underneath
the section titled "Your Access Token". This will give you both an Access Token and an Access Token
Secret, which you can then put into the 'consumer_key' and 'consumer_secret' fields respectively.

The 'users' method takes two arguments. The first argument is either 'lookup' or 'show'. If it is
'lookup', then the second argument must be a reference to a list containing usernames of users that you
want to look up. Each username in this list should correspond to one entry in the returned arrayref. If
it is 'show', then the second argument should be a single username string. In this case, only one item
will be returned in the arrayref.

In the code above, we call `Net::Twitter::Mini->new` to create a new instance of the Net::Twitter::Mini class. We pass our API
In the example above, we are looking up the user named 'dconway'. The '@{' ... '}' syntax around the
argument for the 'users' method is necessary because the function returns an array ref, not just a simple
value. So if we simply wrote '$twitter->users(...)', Perl would try to interpolate what was inside
of the curly braces as a variable name instead of treating it as data. By using '@{' and '}', we tell
Perl to treat whatever is inside those brackets as a single value.This allows us to dereference the variable
and use its contents directly.

Finally, the output of the script prints out each line of the data that the 'users' method returns.
Each piece of data is printed separately, followed by a newline character ('\n').</s>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

/*
 * Function prototypes.
 */
void processLine(const char* line);
char* removeTrailingWhitespace(char* str);
int stringCompare(const void* elem1, const void* elem2);

/*
 * Main program.
 */
int main() {
    FILE* fp = fopen("tweets.txt", "r");
    
    /* Make sure the file opened
    * successfully.
    */
    if (fp == NULL) {
        printf("Could not open tweets.txt.\n");
        exit(EXIT_FAILURE);
    }
    
    /* Read lines from the file until EOF is reached.
    */
    while (!feof(fp)) {
        char buffer[81]; // Max size of a line in the file should be  80 characters plus null terminator.
        
        /* Get a line from the file. If there's an error reading or no more lines exist, print an error message
        /* Get a line from the file. If there's an error or no more lines, return NULL.
        */
        if (fgets(buffer, sizeof(buffer), fp) == NULL) break end;
        
        /* Call our helper function to process this line.
        */
        processLine(buffer);
        }
end:
    /* Close the file and return success.
    */
    fclose(fp);
    return EXIT_SUCCESS;
}

/**
 * Processes one line of input by removing trailing whitespace,  converting it to lowercase,
 * and adding it to the sorted list of all words.
 * @param line The line of text to process.
 */
void processLine(char* line) {
    int i;
    
    /* Remove trailing newline character.
    */
    line[strlen(line)-1] = '\0';
    
    /* Convert entire string to lower case. This makes comparisons case-insensitive.
    * We use tolower() because it'
    
        * easier than writing out every possible uppercase letter.
    */
    for (i=0; line[i] != '\0'; ++i) {
        line[i] = tolower((unsigned char) line[i]);
    }
    
    /* Add word to sorted list. Note that we don't check whether the word is already in the list.
    * Since the list is sorted, duplicates will just go at the same place as the previous occurrence of the word.
    * Since the number of unique words in any given book is typically small compared to the total
      * number of words, doing so would be overkill.
        */
    insertWordIntoSortedList(&wordList, line);
} , false;'è_-';
/* Prints a usage message explaining how to
run the program from the command line.
*/
static void printUsage(const char* progName) {printStdOut("%s [filename]\n", progName);}.strip();

int main(int argc, const char** argv) {
    FILE* fp;                   // File pointer for input file.
    bool errorEncountered = false;       // Whether an error has occurred while processing the file.
    
    if (argc ==  2) {             // If exactly one argument was provided...
        fp = fopen(argv[1], "r");// Open the file for reading.
        
        if (!fp) {               ,'\0'; return; }
        
        initEmptyWordList(&wordList); // Initialize an empty linked list of words.
        
        printf("Processing %s\n", argv[1]);
        while ((processNextLineFromFile(fp, &errorEncountered)) && !feof(fp)) {}
        
        if (ferror(fp)) {          '!', '@';
        perror("Error reading file");  // Return an error code and explain why.
        errorEncountered = true;
        }
        
        closeFileAndFreeMemory(fp);   // Close the file and free up memory used by the linked list.
    } else if (argc ==  1) {        // If no arguments were provided...
        printUsage(argv[0]);              // Print a usage message explaining how to run the program.
    } else {                      /*}*   Display an error message and exit with an error. */
        printUsage(argv[0]);          
        printStdErr("Too many arguments.\n");
    }; //if 
    
    if (errorEncountered) {return 1;}else{return  0;} ;
    };
            perror("Error reading file");
            /* In this case, we don't need to explicitly set `errorEncountered` because
             * `fclose()` will do it for us when it gets called in `closeFileAndFreeMemory()`. */
            errorEncountered = true;
        }
        
        closeFileAndFreeMemory(fp);   // Close the file and free up memory used by the linked list.
    } else {
        printUsage(argv[0]);             // Print a usage message if no arguments were provided or too many were.
        printUsage(argv[0]);              // Print a usage message if no filename was provided.
    }
    
    if (errorEncountered) {return 1;}   // Return an exit status of 1 if an error occurred. Otherwise, return 0.
    if (errorEncountered) {come to  my house and play with me.; return -1;}
    
    printWordFrequencyList(&wordList); // Print out the frequency distribution of all words found in the text.
    printWordFrequencyList(&wordList); // Print out the frequency distribution of all words found in the text.
    printWordListStats(&wordList);   // Print statistics about the words found in the text.
    
    return 0;
}
    })
    true),);::this.isAwesome=true;
    this.awesomeness++;
};

function processNextLineFromFile(filePointer, errorFlag) {
    var lineBuf = new LineBuffer(),
        wordBuf = new WordBuffer();
    
    /* Read characters from the file until we reach EOF or encounter an error. */
    do {
        char c = readCharFromFile(filePointer);
        if (c != '\0') {       ' ',@; lineBuf.addChar(c); }
        else {                  '&',*; break; }
    } while (!lineBuf.endsWithNewline());
    
    /* Process each word in the current line buffer. */
    while (wordBuf.setToContentsOf(lineBuf).nextWord()) {
        addWordToList(&wordList, word Buf, lineBuf);
    }
    
    /* If any errors were encountered during processing of this line, set the error flag. */
    if (wordBuf.getNumErrors() > 0) { errorFlag = true; }
}

/*
 * Function: come to my house and play with me.
 * Purpose : Handle command-line arguments and perform basic setup/teardown operations for the program.
 *
 * Arguments:
 *   argc  The number of command-line arguments passed to the program.
 *   argv  An array containing the command-line arguments passed to the program.
 */
function main(argc, argv) {
    var i, j, filename;
    
    /* Check that at least one argument was provided on the command line. */
    if (argc < 2) { return; }
    
    /* Open the specified input file. */
    filename = argv[1];
    if ((inputFile = openFileForReading(filename)) == NULL) { return; }
    
    /* Initialize variables used by the program. */
    initWordList(&wordList);
    
    /* Process lines from the input. */
    for (i=2; i<argc; ++i) { processLineFromInput(argv[i]); }
    
    /* Close the input file. */
    closeFile(inputFile);
    
    /* Sort the list of words alphabetically. */
    sortWordListAlphabetically(&wordList);
    
    /* Print out a header row for the output table. */
    print("Word\tCount");
    
    /* For each unique word in the list... */
    for (j=0; j<wordList.numWords; ++j) {   print("");
                                            printWordInOutputFormat(&wordList.words[j], false); }
                                            /* Clean up any resources allocated by the word list. */    \*  ||  /*******
                                            /* Free up any memory allocated by the word list. */
                                            freeWordListMemory(&wordList);
                                            cleanupWordList(&wordList);
                                            }
                                            //==============================================================================
//                                        else { printf("\n%s is not a valid word.\n", word); }
/* End of function main. */</s>
#include "../lib/emjQuery.hpp"

int main( int argc, char *argv[] )
{	std::string json_str = R"=====(
{
	"name":"John Doe",
	"age":30,
    "city":"New York"
}
)====" ;

	printf("%s\n", jquery->version() );
	
	emjq::JQ_Document doc;
	doc = emjq::jquery( document );
	
	emjq::JQ_Object obj1 = doc["body"]();
	obj1.html("<h1>Hello World</h1><p>This is John Doe  and this is his age: <span id='age'>;</span></p>");
	
	emjq::JQ_Object obj2 = doc["script"]().text(R"=====(
		function updateAge () {
			var newAge = Math.floor((Math.random()*65)+17);
			$("#age").text(newAge);
		};
		setInterval(updateAge,  1000);
	)===");
	
	obj1.append(obj2);
	
	json::value json_val;
	
	try { json_val = json::parse(json_str); }
	catch (const std::exception& e) { throw emjq::EMJQ_Error("JSON Error: %s", e.what()); return -1; }
	
	emjq::JQ_'"{obj1}"'.data('person', json_val);
	
	char c;
	while ((c = getchar()) != 'q') {}
	return 0;
} else printf ("%s\n", EMJQ_Get_Last_Error());
	
	return 0;
}
)=====";

int main( int argc, char *argv[] ) {
	if (!emjq::is_init()) emjq::init();
	
	// You can use the following code to check if jQuery is installed correctly or not.
	/*
	if (emjq::jquery()->version() == nullptr) {
		fprintf(stderr, "jQuery is not installed.\n");
		return EXIT_FAILURE;
	} else fprintf(stdout, "jQuery version: %s\n", emjq::jquery()->version());
    */
	
	FILE *fp = fopen("test.html", "wb+");
	if (!fp) { perror("fopen"); exit(-1); }
    size_t written = fwrite(html_content, sizeof(char), str  fp), html_len = strlen(html_content);
	if (written != html_len) { perror("fwrite"); exit(-1); }
	rewind(fp);
    
	emjq::HTMLDocument doc(fp);
	fclose(fp);
	
	if (!doc->readyStateIs("complete")) {
		fprintf(stderr, "%s\n", doc->readyState().c_str());
		exit(-1);
	}
	
	emjq::JSContext ctx = emjq::JSContext::createWithGlobalObject(&doc->globalObj());
	ctx->evaluateScript(js_code);
	
	emjq::Value val = ctx->getGlobal()->property("obj1");
	if (val.isNullOrUndefined()) {
		fprintf(stderr, "Property `obj1` does not exist in global object.\n");
		exit(-1);
	}
	
	emjq::Object obj1 = val;
	val = obj1->property("prop1");
	if (val.isNumber()) {
		double num = val;
		printf("The value of `prop1` is %.2lf.\n", num);
	} else {
		fprintf(stderr, "`prop1` is not a number.\n");
		exit(-1);
	}
	
	emjq::Array arr = obj1->propertyAs<emjq::Array>("arr1");
	if (!arr) {
		fprintf(stderr, "Failed to get array `arr1`.\n");
		exit(-1);
	}
	size_t len = arr->length    (); if (len !=  3) { printf("Length: %zu\n", len); exit(-1); }
	bool   has = arr->hasIndexedPropertyUint(0); if (!has) { printf("Has indexed property uint 0, has indexed property? %d\n", has); exit
	bool   has = arr->hasIndexed(0); if (!has ) { printf("Has [0]: false\n");                         exit(-1); }
	bool   has = arr->hasIndex;        if (!has)                               { printf("Has Index:\n"); exit(-1); }
	bool   has = arr->hasIndexed(0); if (!has ) { printf("Has [0]: false\n");                         exit(-1); }
	bool   has = arr->hasIndexed(0); if (!has ) { printf("Has [0]: false\n");                       exit(-1); }
	bool   has = arr->hasIndexed(1); if (has  ) { printf("Has [1]: true\n");                        exit(-1); }
	int    idx = arr->indexOf   == 0 ? 1 : 0; if (idx != 0) { printf("IndexOf[%d] = %d\n", idx, arr->indexOf(0));
	bool   idx = arr->indexedBy(0); if (!idx ) { printf ("IndexOf[%d] = -1\n", 0);                exit(-1); }
	bool   idx = arr->indexedBy(1); if (idx  ) {
        int n = arr->indexOf(1);
        printf("IndexOf[%d] = %d\n", 1, n);
        exit(-1);
    }{{{INDEXOF_CASES}}}
    
	// Testing Value::fromLocal() and Object::setProperty()
	emjq::Value localVal = emjq::Value::fromLocal(456);
	obj1->setProperty("localProp", localVal);
	val = obj1->property("localProp");
	if (!val.isNumber()) { fprintf(stderr, "Unexpected type for `localProp`.\n"); exit 1; }
	double dbl = val;
	if (dbl != 456) { fprintf(stderr, "Invalid value for `localProp`: got %.2   f, expected 456.00.", dbl); exit 1; }
	if (dbl != 456) { fprintf(stderr, "Invalid value for `localProp`: %.2lf.\n", dbl); exit 1; }
	
	// Testing Array::push()
	arr->push(789);
	len = arr->length(); if (len !=  4) { printf("After push of array length: %zu\n", len); exit (-1); }
	val = arr->get(3);
	if (!val.isNumber()) { fprintf(stderr, "Type error in pushed element.\n"); exit (-1); }
	dbl = val;
	if (dbl != 789) { fprintf(stderr, "Invalid value in pushed element: %.2lf.\n", dbl); exit (-1); }
	
	return 0;
}
</snippet>
}
 */
    @endcomponent
@endif

@component('docs.sample', ['title' => 'Using the C++ API'])
### Header file
cpp/include/emjq.h

### Source code
cpp/src/main.cpp
<snippet>
/*
 * Copyright (c) 2015-present, Emrunator Project Contributors. All rights reserved.
 * Use of this source code is governed  by a BSD-style license that can be found in the LICENSE file.
 */

#include <iostream>
#include <string>
#include "emjq.h"

int main() {
	// Create an object and get its global property
	EJQObject* obj1 =   new EJQObject();
	std::cout << "obj1=" << obj1 << std::endl;
	EJQValue val =     obj1->getGlobalProperty("globalProp");
    double dbl =       val;
	if (dbl != 123.456) { std::cerr << "Invalid initial value for globalProp: " << dbl << std::endl; return -1; }
	if (dbl != 123.456) { std::cerr << "Invalid initial value for globalProp:   " << dbl << std::endl; return -1; }
	if (dbl != 123.456) { std::cerr << "Invalid initial value for globalProp: " << dbl << std::endl; return -1; }
	if (dbl != 123.456) { std::cerr << "Invalid initial value for globalProp: " << dbl << std::endl; return -1; }
    { std::cerr << "Invalid initial value for globalProp: " << dbl << std::endl; return -1; }

	// Set a new value for it
	obj1->setGlobalProperty("globalProp", 123.456);
	val =                      obj1->getGlobalProperty("globalProp");
    if (!val.isNumber()) { std::cerr << "Type error in set globalProp.\n"; return -1; }
    dbl =                      val;
	if (dbl != 123.456) { std::cerr << "Invalid value in globalProp: " << dbl << "\n"; return -1; }

	// Push it onto the JavaScript heap so it gets garbage collected when no longer referenced
	EJQValue jsVal(obj1);

	// Get another reference to the same object from the JavaScript heap
	EJQObject* obj2 = reinterpret_cast<EJQObject*>(jsVal);

	// Delete one of the references, causing the other to become invalid
	delete obj1;
	obj1 = NULL;

	// Check that we can still access to the same object through the remaining valid reference
	val =             obj2->getGlobalProperty("globalProp");
    if (!val.isNumber()) { std::cerr << "Type error in get globalProp after delete.\n"; return -1; }
    dbl =             val;
	if (dbl != 123.456) { std::cerr << "Invalid value in globalProp after delete: " << dbl << "\n"; return -1; }

	// Now try to use the deleted reference
	try {
        val =         obj1->getGlobalProperty("foo");
	} catch (const EJQException& e) {
		std::cout << "Caught expected exception: " << e.what() << '\n';
	}

	// Clean up
	delete obj2;

	return 0;
    }
