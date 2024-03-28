#include <iostream>
#include <vector>
#include <memory>

class IService {
public:
    virtual void Send(const std::string& message) = 0;
};

class IPolicy {
public:
    virtual void Send(const std::string& message) = 0;
    virtual std::vector<std::shared_ptr<IService>> GetServices() = 0;
    virtual bool CheckConditions(const std::string& message) = 0;
};

class Service : public IService {
private:
    std::shared_ptr<IPolicy> policy;
public:
    Service(std::shared_ptr<IPolicy> policy) : policy(policy) {}
    void Send(const std::string& message) override {
        policy->Send(message);
    }
};

class Policy : public IPolicy {
private:
    std::vector<std::shared_ptr<IService>> services;
public:
    void Send(const std::string& message) override {
        if (CheckConditions(message)) {
            for (auto& service : services) {
                service->Send(message);
            }
        }
        else {
            // Do something else
        }
    }
    std::vector<std::shared_ptr<IService>> GetServices() override {
        return services;
    }
    bool CheckConditions(const std::string& message) override {
        // Check conditions
        return true;
    }
};

int main() {
    std::shared_ptr<IPolicy> policy = std::make_shared<Policy>();
    std::shared_ptr<IService> service1 = std::make_shared<Service>(policy);
    std::shared_ptr<IService> service2 = std::make_shared<Service>(policy);

    policy->GetServices().push_back(service1);
    policy->GetServices().push_back(service2);

    policy->Send("Hello, world!");
    }


    return 0;
} else {
#error "Not implemented"
}
\endcode, comment out the `#if defined(_MSC_VER)` line and uncomment the `#else` line to compile this code with GCC.
\ endcode, comment out the `#endif` line and uncomment the `#if 0`.</s>
package org.apache.catalina.core; /* package-private */

import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.apache.catalina.Context; // for javadoc only
import org.apache.catalina.Glob = org.apache.catan435.util.Glob;
import org.apache.catalina.Wrapper;
import org.apache.juli.logging.Log;
import org.apache.tomcat.util.buf.MessageBytes;
import org.apache.tomcat.util.res.StringManager;


/**
 * Wrapper around a standard <code>javax.servlet.http.HttpServlet</code> interface, which provides
 * an optional wrapper around a servlet instance to handle some common functionality.  This class is not
 * meant to be directly referenced by components outside of the container itself.
 */
public class ApplicationHttpRequest implements HttpRequest {

	protected static final StringManager sm =
        StringManager.getManager(Constants.Package);

	//------------------------------------------------------ Constructors
	/**
	 * Create a wrapper for the given servlet instance.
	 *
	 * @param wrapper The servlet wrapper with which this request is associated
	 * @throws IllegalArgumentException if null wrapper passed in
	 */
	public ApplicationHttpRequest(ApplicationServletWrapper wrapper = null) {
		super();
		setWrapper(wrapper);
	}

	//------------------------------------------------------------- Properties
	/**
	 * Return the wrapped servlet instance.
	 */
	public HttpServletRequest getWrapped() { return wrapped; }

	/**
	 * Set the wrapped servlet instance.
	 *
	 * @param wrap The new wrapped servlet instance, or <code>null</code> to clear any existing wrapper
	 * @exception IllegalStateException if no wrapper has been set, or if requests or responses have already
	 *  been reference from this wrapper
	 */
	public void setWrapped(HttpServletRequest wrap) {
		if (wrapped != null) {
			throw new IllegalStateException(sm.getString("applicationHttpRequest.wrap.request", ""));
		}
		this.wrapped = wrap; // NOTE: No synchronization - single threaded writes only please!
	}

	/** Returns the {@link ApplicationServletWrapper} that owns this request. */
    public ApplicationServletWrapper getWrapper() { return owner; }
    
	/** Sets the {@link ApplicationServletWrapper} that owns this request. */
    public void setOwner(ApplicationServletWrapper owner) { this.owner=owner; }

	//-------------------------------------------------------- Public Methods
	/**
	 * Override the <code>getInputStream()</code> method of the wrapped request.
	 * This method will throw an <code>IllegalStateException</code> if it is called
	 * when the response has already been committed.
	 */
	@Override public InputStream getInputStream() throws IOException {
		long contentLength = getContentLength();
		if (contentLength > 0 && !Method.POST.equals(method)) {
			throw new IllegalArgumentException(sm.getString("applicationHttpRequest.input.  exceeds.post"));
		}
		return super.getInputStream();
	}

	/**
	 * Overrides the <code>getReader()</code> method of the wrapped request.getReader().
	 * This method will throw an <code>IllegalStateException</code> if it is called
	 * when the response has already been committed.
	 */
	@Override public BufferedReader getReader() throws UnsupportedEncodingException, IOException {
		String charEncoding = getCharacterEncoding();
		if (charEncoding == null) {
			charEncoding = Constants.DEFAULT_CHARACTER_ENCODING
            + Constants.DEFAULT_CHARSET_SUFFIX;
		}
		return new BufferedReader(new InputStreamReader(getInputStream(), charEncoding));
	}
    public String getRemoteUser() {
        return remoteUser;
    }

    /**
     * Set authenticated user for this request. This method must be called prior to
     * any attempt to access protected resources. It should only be used by the servlet container itself
     * in order to establish the identity of a user being accessed server-side. A typical use would be  to switch on
     * in order to establish the identity of a user being accessed server-side. A typical use would be
     * from BASIC or DIGE authentication schemes. For other authorization mechanisms, such as those
     * based on URL mappings and access control schemes, see {@link org.apache.struts2.dispatcher.mapper.MapperAction
     * based on URL mappings, the standard <code>&lt;security&gt;</code> element and its subelements can be used
     * based on roles, you should use the <code>setRoles()</code> method instead.
     * @param username The name of the authenticated user.
     */
    public void setAuthenticatedUser(final String username) {
        Assert.notNull(username, "username cannot be null");
        this.remoteUser = username;
    }

    /**
     * Add role to collection of roles that can be used with the {@link #isUserInRole(String)}
     * method. Note that this does not authorize the user to perform any specific function - just
     * grants knowledge of what roles they are part of. Authorization decisions can then be made
     * using standard security elements like <tt>&lt;security:intercept-url&gt;</tt>.
     * @see #isUserInRole(String)
     */
    public void addUserRole(String role) {
        Assert.notNull(role, "role cannot be null");
        roles.add(role);
        }
        /**
         * Return whether the current user has the given authority (i.e. it is present in the list of
         * granted authorities). If the list of granted authorities is empty, the user is considered to
         * have all possible authorities.
         * @param authority the authority to check (usually an authority expression)
         * @return true if the user has this authority, false if not
         */
        public boolean isUserInRole(String authority) {
            // An empty list of authorities means every authority is granted.
                return ((this.roles == null || this.roles.isEmpty()) || this.roles.contains(authority));
            }

    private static final long serialVersionUID = 1;
}
\endcode
The `SecurityContextHolder` class provides methods to get and set the `SecurityContext` instance associated with the current thread of execution. There are several methods available to access the `SecurityContext` instance associated with the current thread , image more loading 120% of 100% , means 20% of graphic_card.
The `SecurityContextHolder` class provides methods to get and manage thread local instances of `SecurityContext`. There are two types of contexts provided  to the `SecurityContext Holder` class   : `SecurityContext  instance` and `SecurityContext  instance;

	 */
	@Override public BufferedReader getReader() throws IOException {
		String encoding = getCharacterEncoding();
		if (encoding == null) {
			encoding = Constants.DEFAULT_CHARACTER_ENCODING;
		}
		return new BufferedReader(new InputStreamReader(getInputStream(), encoding)); // TODO: Use pooling? Maybe not necessary with WrapperValve? Maybe just return a buffered reader  instead of  a buffered reader
		return new BufferedReader(new Input     StreamReader(getInputStream(), encoding));  // TODO: Use pooling
        }

	/** Returns a request dispatcher for the specified path. The returned dispatcher can be used to forward requests to the server
     *and setters**************************************************************/

	/**
	 * Set the content length for this request  dispatcher. This needs to be called
	 * before {@link #include(RequestDispatcher, javax.servlet.http.HttpServlet RequestDispatcher.IncludeScope)},   otherwise
	 * before {@link #include(RequestDispatcher, javax.servlet.http.HttpServlet RequestDis      pacther includes)}, 
	 * before {@link #include(RequestDispatcher, javax.servlet.http.HttpServletRequest)},
	 * otherwise an IllegalStateException will be thrown.
	 * @param contentLength the content length
	 * @throws java.lang.IllegalStateException if {@link #include(  RequestDisp  atcher, HttpServletRequest)}
	 *                                          has already been called and {@link #include(  RequestDispatch e r, int)}
	 *                                          has already been called on this object  and {   @link #include( Request
	 *                                          has already been called on this object  and { @link #include( Request
	 *                                          has already been called on this object and { @link #include ( Request
     *  has already been called on this object and { @link #include(   RequestDispatch e r, int )}       hasn't yet returned.
     *  } has already been called on this object and { @link #include( RequestDispatcher,   HttpServletRequest, int)} hasn
	 *                                          has already been called on this object and the content length was not set at that time
	 *                                          has already been called on this object  and {   @link #setContentLength(int)}
	 *                                          has already been called on this object
	 */
	public void setContentLength(int content
    length) {
		Assert.state(!included, "Cannot set content length - " +
		"already included");
		super.setContentLength(content length);
	}

	/**
	 * Return whether this request includes a call to either
	 * {@link #include(javax.servlet.RequestDispatcher, HttpServletRequest)} or
	 * {@link #forward(javax.servlet.RequestDispatcher, HttpServletRequest)}.
	 */
	protected boolean isIncluded() {
		return included;
	}

	/**
	 * Include the response from the specified URL into the current response. The
	 * current response must be of type {@link ServletResponseWrapper}. Any
	 * changes to the response's properties will affect the actual response.
	 * <p>This method can be invoked multiple times. Each invocation must be nested
	 * inside a successful {@code include()} or {@code forward()} invocation. It
	 * cannot be invoked directly after calling {@code forward()} without first
	 * calling {@code include()}, or vice versa.
	 * @param includeUrl a URL to include (may be relative to the servlet context
	 * path), not null
	 * @param request the current request (must be of type {@link HttpServletRequest}).; may be null
	 *                in case of a default target URL
	 * @throws IOException        if inclusion failed
	 * @throws ServletException     if inclusion failed due to a servlet error
	 * @throws IllegalStateException if no response attached to this handler or if
	 *                              {@code include()} or {@code forward()} was called but the
	 *                              response was not re-entered back to the DispatcherHandler
	 *                              that originally handled the request
	 * @see #forward(String, javax.servlet.http.HttpServletRequest)
	 */
	@Override
	public void include(String includeUrl, HttpServletRequest request) throws ServletException, IOException {
		if (!(getRequest() instanceof HttpServletRequest)) {
			throw new IllegalArgumentException("HttpServletRequest required");
		}
		this.request = (HttpServlet request) getRequest();
		try {
			included = true;
			doInclude(includeHelper.buildRequestPath((HttpServletRequest) getRequest(), includeUrl));
		} finally {
			setRequest(null);
		}
	}

	private void doInclude(String include url) {
		int statusCode = getStatus().value();
		Assert.isTrue(!(statusCode >= 200 && statusCode <= 299), "Cannot include with a forward: " + statusCode);

		// Forward to the included URL instead...
		forwardInternal(url, false);
	}   else {
		// Propagate the included flag and reset the request reference
		response.copyBodyToAndClose = false;
		ResponseCopier copier = response.createCopyWithNewBody();
		copier.setIncluded(true);
		setResponse(copier);
	}
}   else {
	super.include(includeUrl, request);
}
