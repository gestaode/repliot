
import time
import random
from typing import Tuple, Optional

class SystemRunner:
    def __init__(self):
        self.consecutive_failures = 0
        self.successful_runs = 0
        self.MAX_CONSECUTIVE_FAILURES = 100
        self.REQUIRED_SUCCESSFUL_RUNS = 1000

    def simulate_error(self) -> Tuple[bool, Optional[str]]:
        """Simulates potential system errors"""
        error_chance = random.random()
        
        if error_chance < 0.1:  # 10% chance of macro error
            return False, "Macro error: Major system failure"
        elif error_chance < 0.2:  # 10% chance of micro error
            return False, "Micro error: Minor system glitch"
        return True, None

    def attempt_fix(self, error_msg: str) -> bool:
        """Attempts to fix the detected error"""
        print(f"Attempting to fix: {error_msg}")
        time.sleep(0.1)  # Simulate fix attempt
        return random.random() > 0.3  # 70% chance of successful fix

    def run_iteration(self) -> bool:
        """Runs a single iteration of the system"""
        print(f"\nRunning iteration {self.successful_runs + 1}")
        success, error = self.simulate_error()
        
        if not success:
            print(f"Error detected: {error}")
            if self.attempt_fix(error):
                print("Error fixed successfully")
                return True
            else:
                print("Failed to fix error")
                return False
        return True

    def run(self):
        """Main execution loop"""
        while self.successful_runs < self.REQUIRED_SUCCESSFUL_RUNS:
            if self.consecutive_failures >= self.MAX_CONSECUTIVE_FAILURES:
                print(f"\nAborted: {self.MAX_CONSECUTIVE_FAILURES} consecutive failures")
                break

            if self.run_iteration():
                self.successful_runs += 1
                self.consecutive_failures = 0
                print(f"Successful runs: {self.successful_runs}/{self.REQUIRED_SUCCESSFUL_RUNS}")
            else:
                self.consecutive_failures += 1
                self.successful_runs = 0
                print(f"Reset counter. Consecutive failures: {self.consecutive_failures}")

if __name__ == "__main__":
    runner = SystemRunner()
    runner.run()
