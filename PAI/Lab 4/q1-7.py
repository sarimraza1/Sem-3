# Question 1
class ThreatDetector:
    def __init__(self, device_name, ip_address, threat_level):
        self.device_name = device_name
        self.ip_address = ip_address
        self.threat_level = threat_level

    def scan(self):
        if self.threat_level == "Low":
            print(self.device_name, ":", "System Safe")
        elif self.threat_level == "Medium":
            print(self.device_name, ":", "Suspicious Activity")
        elif self.threat_level == "High":
            print(self.device_name, ":", "Critical Threat Detected")


device1 = ThreatDetector("CS1", "192.168.0.1", "Low")
device2 = ThreatDetector("CS2", "192.168.0.2", "Medium")
device3 = ThreatDetector("CS3", "192.168.0.3", "High")

device1.scan()
device2.scan()
device3.scan()



# Question 2


class PasswordVault:
    def __init__(self, username, password):
        self.username = username
        self._vault_status = "Locked"
        self.__password = password

    def change_password(self, new_password):
        self.__password = new_password
        print("pass changed")

    def verify_password(self, entered_password):
        if entered_password == self.__password:
            print("Access Granted")
        else:
            print("Access Denied")

    def display_status(self):
        print("Status:", self._vault_status)


vault = PasswordVault("admin", "admin123")
vault.display_status()
vault.verify_password("haha")
vault.verify_password("admin123")
vault.change_password("admin234")
vault.verify_password("admin234")



# Question 3


class SecuritySystem:
    def respond(self):
        print("responding to cyber attack")


class Firewall(SecuritySystem):
    def respond(self):
        print("blocking suspicious network traffic")


class Antivirus(SecuritySystem):
    def respond(self):
        print("isolating malicious files")


class IntrusionDetectionSystem(SecuritySystem):
    def respond(self):
        print("generating security alert")


systems = [Firewall(), Antivirus(), IntrusionDetectionSystem()]

for system in systems:
    system.respond()



# Question 4


class Robot:
    def __init__(self, name, battery):
        self.name = name
        self.battery = battery

    def move(self):
        if self.battery >= 20:
            print(self.name, "in action")
        else:
            print(self.name, "cannot move as battery is below 20%")

    def charge(self):
        self.battery = 100
        print(self.name, "is charged 100%")


class DeliveryRobot(Robot):
    def move(self):
        if self.battery >= 20:
            print(self.name, "moves to a delivery location")
        else:
            print(self.name, "cannot move as battery is below 20%")


class SecurityRobot(Robot):
    def move(self):
        if self.battery >= 20:
            print(self.name, "patrols a specific area")
        else:
            print(self.name, "cannot move as battery is below 20%")


class RescueRobot(Robot):
    def move(self):
        if self.battery >= 20:
            print(self.name, "moves toward a disaster location")
        else:
            print(self.name, "cannot move as battery is below 20%")


robot1 = DeliveryRobot("Delivery Robot", 80)
robot2 = SecurityRobot("Security Robot", 50)
robot3 = RescueRobot("Rescue Robot", 15)

robot1.move()
robot2.move()
robot3.move()
robot3.charge()
robot3.move()




# Question 5


class Agent:
    def __init__(self, name, status):
        self.name = name
        self.status = status

    def perform_task(self):
        print("performing a task")


class SecurityAgent(Agent):
    def perform_task(self):
        print(self.name, ":", "Detecting cyber threat")


class MonitoringAgent(Agent):
    def perform_task(self):
        print(self.name, ":", "Monitoring system activity")


class RecoveryAgent(Agent):
    def perform_task(self):
        print(self.name, ":", "Recovering system services")


agents = [
    SecurityAgent("Security Agent", "Active"),
    MonitoringAgent("Monitoring Agent", "Active"),
    RecoveryAgent("Recovery Agent", "Active")
]

for agent in agents:
    agent.perform_task()




# Question 6

class Computer:
    def __init__(self, cpu_usage, ram_usage, battery_level):
        self.cpu_usage = cpu_usage
        self.ram_usage = ram_usage
        self.battery_level = battery_level

    def system_status(self):
        if self.cpu_usage <= 80 and self.ram_usage <= 85 and self.battery_level >= 20:
            print("working fine")
        else:
            if self.cpu_usage > 80:
                print("Heavy CPU Load")
            if self.ram_usage > 85:
                print("High Memory Usage")
            if self.battery_level < 20:
                print("Low Battery")


computer1 = Computer(90, 70, 15)
computer2 = Computer(50, 90, 60)

computer1.system_status()
computer2.system_status()




# Question 7


class CyberAgent:
    def __init__(self, agent_name, status, threat_score):
        self.agent_name = agent_name
        self.status = status
        self.__threat_score = threat_score

    def update_threat_score(self, score):
        self.__threat_score = score

    def get_threat_score(self):
        return self.__threat_score


class NetworkAgent(CyberAgent):
    def analyze(self):
        print(self.agent_name, ":", "analyzing traffic")

    def respond(self):
        print(self.agent_name, ":", "blocking suspicious activity")


class MalwareAgent(CyberAgent):
    def analyze(self):
        print(self.agent_name, ":", "analyzing malicious software")

    def respond(self):
        print(self.agent_name, ":", "isolating malicious files")


class IncidentResponseAgent(CyberAgent):
    def analyze(self):
        print(self.agent_name, ":", "analyzing security incident")

    def respond(self):
        print(self.agent_name, ":", "starting incident response")


agent1 = NetworkAgent("Network Agent", "Active", 70)
agent2 = MalwareAgent("Malware Agent", "Active", 85)
agent3 = IncidentResponseAgent("Incident Response Agent", "Active", 90)

agent1.analyze()
agent1.respond()

agent2.analyze()
agent2.respond()

agent3.analyze()
agent3.respond()

print("Threat Score:", agent1.get_threat_score())
agent1.update_threat_score(80)
print("Updated Threat Score:", agent1.get_threat_score())
