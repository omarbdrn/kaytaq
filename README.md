# kaytaq
RSS Feed Monitoring to feed blog posts into KayTaq for blog creations.

# Sample Output
Running it on [CyberDanube Security Research 20230511-0 | Multiple Vulnerabilities in Advantech EKI-15XX Series](https://seclists.org/fulldisclosure/2023/May/4)
```
A security research report by CyberDanube highlights multiple vulnerabilities found in Advantech EKI-15XX series products, which are commonly used for industrial IoT applications. The vulnerabilities include two instances of authenticated command injection and a buffer overflow, which could allow an attacker to take full control of the affected systems. The vulnerable versions are 1.21 of the EKI-1524, EKI-1522, and EKI-1521 models. The vendor has provided fixed firmware versions (1.24) to address the issues, and customers are advised to upgrade 
as soon as possible. The full contact timeline, detailing the communication between CyberDanube and Advantech, is also available.

According to Advantech's corporate vision, the company aims to enable an intelligent planet by providing IoT intelligent systems and embedded platforms. However, this vision can be undermined when its products contain serious security flaws. In the case of the EKI-15XX series, an attacker who gains access to the device's web server could execute arbitrary commands with root privileges, which could cause a wide 
range of damage, including data theft, device disruption, and network compromise.

The proof of concept for the command injection vulnerability shows how an attacker could leverage the NTP server and device name fields in a POST request to inject and execute commands such as "ping" and "ls" on the affected systems. The buffer overflow vulnerability can be triggered by sending a long NTP server string, causing the underlying 
operating system to crash or malfunction.

CyberDanube's researchers used an emulated device and the MEDUSA scalable firmware runtime to test and verify the vulnerabilities. The researchers also tried to contact Advantech via its service request form and its Czech PSIRT, but got no response initially. After some back-and-forth communication, the vendor acknowledged the vulnerabilities 
and provided a beta release and then a full firmware update to fix them.

It's worth noting that the vulnerabilities could have been discovered and exploited by other actors before the vendor could provide a fix, especially if the affected systems were internet-facing or had unsecured remote access. Therefore, it's essential for customers to follow the recommended best practices for industrial IoT security, such as 
applying security patches promptly, restricting network access, monitoring system logs, and conducting security audits and assessments regularly.

References:
- https://seclists.org/fulldisclosure/2023/May/4
- https://www.cyberdanube.com/
```
