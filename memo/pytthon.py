<,.',',?,.:://::',/*'
// 							 2. Remove any remaining entries that are not valid URLs (e.g., "http:/google.com" or "www.google.com").
// 							 1. Remove any characters that are not letters, numbers or spaces that are not valid characters for a URL (such as punctuation).
// 12345678901234567890123456789012345678901234567890123456789012345678901234567890

#include "config.h"

#ifdef HAVE_UNISTD_H
# include <unistd.h>
#endif /* HAVE_UNISTD_H */
#include <stdio.h>
#include "gu.h"
#include "global_defines.h"/* global defines */
#include "libppr_private.h"/* private ppr entries, also used by ppad */

/**
 * This is the main entry point for the PPR daemon.  It initializes various
 * things and then calls one of two functions: start_daemon() or start_service().
 */
int main(void)
	{
	char buf[MAX_PPR_COMMAND];
	const char *command;

	/* initialize the library */
	gu_library_init();

	/* get the command name from the environment */
	command = gu_getenv("PPRAUTO_CMD");
	if(!command)
		{
		fprintf(stderr, "%s: Environment variable PPRAUTO_/%s not set\n", argv0, "PPRAUTO_CMD");
    return EXIT_FAILURE;
		}
  /* If we are running as a service under systemd, tell it that we have started. */
#if defined(SYSTEMD_SERVICE)
	sd_notify(0, "STATUS=Started");
#endif

	/* if the command starts with "start-", call start_daemon(), otherwise call start_service() */
	if(strncmp(command, "start-", strlen("start-")) == 0)
		{
		gu_strlcpy(buf, &command[strlen("start-")], sizeof(buf));
		return start_daemon(buf);
		}
	else
		{
		return start_service(command);
		}
	},

/* end of file                                             */
