<%
    response.setHeader("Strict-Transport-Security", "max-age=63072000; includeSubDomains");
    response.setHeader("X-Content-Type-Options", "nosniff");
    response.setHeader("X-Frame-Options", "DENY");
    response.setHeader("Content-Security-Policy", "default-src 'self'; script-src 'self'; style-src 'self';");
    response.setHeader("Referrer-Policy", "no-referrer");
%>
