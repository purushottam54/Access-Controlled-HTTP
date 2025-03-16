# 🚀 Secure Access-Controlled HTTP Server with User Info Logging

## 🔥 Overview

This Python script creates a **secure** HTTP server with access control, allowing the server owner to manually grant or deny requests. It now includes **IP logging, hostname resolution, device identification, and security features like rate limiting and IP whitelisting** to protect against unauthorized access.

## ⚙️ How It Works

1. **Server Initialization**:
   - Starts on port `8000` and listens for incoming HTTP requests.

2. **Client Request Handling**:
   - Logs the **client IP, hostname (username), and device (User-Agent)**.
   - Displays the **requested file path**.

3. **Security Checks**:
   - Enforces **IP Whitelisting** (optional) to allow only trusted IPs.
   - Implements **Rate Limiting** to prevent excessive requests from the same IP.
   - Logs and monitors all incoming requests for auditing purposes.

4. **User Authorization**:
   - Server prompts for approval before serving the request.
   - If no response is received within **10 seconds**, access is automatically denied.

5. **Response to Client**:
   - If access is granted (`y`), the file is served.
   - If access is denied (`n`) or times out, the client receives a `403 Forbidden` response.

## 🔐 Enhanced Security Features

- ✅ **IP Logging**: Records **IP, hostname, and device details** for each request.
- 🔍 **Hostname Resolution**: Identifies the client's **computer name** (if available).
- 📱 **Device Detection**: Extracts **User-Agent** from HTTP headers (browser, OS info, etc.).
- ✅ **IP Whitelisting**: Only allows predefined trusted IPs to connect (**optional**).
- 🚨 **Rate Limiting**: Blocks excessive requests from a single IP within a minute.
- ⏳ **Timeout Handling**: If no response within `10 seconds`, access is denied automatically.
- 📜 **Request Logging**: Keeps track of denied and granted requests for auditing.
- ⚡ **Threaded Input Handling**: Ensures the server doesn’t freeze while waiting for user input.

## 🛠️ Installation & Usage

1. Save the script as `server.py`.
2. Run the script using:
   ```bash
   git clone  git@github.com:purushottam54/Access-Controlled-HTTP.git
   ```
   ```bash
   python server.py
   ```

3. The server will listen for requests and enforce security policies before responding.

## 🛑 Example Output

```
🔓 Incoming request from: 192.168.1.100 (Johns-PC)
📱 Device Info: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36
📄 Requested Path: /index.html
Grant access to 192.168.1.100 (Johns-PC)? (y/n): y
✅ Access granted to 192.168.1.100 (Johns-PC)
```

## 🛑 Limitations & Considerations

- Requires manual approval for each request, making it less suitable for high-traffic environments.
- Runs on port `8000` by default but can be changed in the script.
- Ensure Python 3.x is installed before running the script.
- Modify `WHITELISTED_IPS` and `RATE_LIMIT` in the script to adjust security settings.

## 🛡️ Prevention Tips

To enhance security while using this script:
- **Be cautious** of unknown IP addresses requesting access.
- **Monitor logs** to detect suspicious activity.
- **Use a firewall** to restrict access to trusted IPs.
- **Keep software updated** to protect against vulnerabilities.

---

https://github.com/user-attachments/assets/ed819aaa-a568-4a53-9520-78c390f68e22
