import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "***Please Drink Water...",
            message="The national academics of scince of engineering has determined that adequate amount of wateris: About 15.5 cups",
            timeout=10                  #timeout in seconds
            
        )
        time.sleep()                    #time in seconds
    
