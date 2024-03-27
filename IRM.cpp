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