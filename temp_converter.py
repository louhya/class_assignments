wantout = 'yes'
while wantout == 'yes':
    tempF = float(input('Please enter the temperature in Fahrenheit ')) #Ask the user to enter the temperate in Fahrenheit
    tempC = (tempF - 32) / (9/5)  #Convert the temperature from Fahrenheit to Celsius
    print("The temperature is %.2f in Fahrenheit and %.2f in Celcius" %(tempF,tempC))  #Display the temperature in both Fahrenheit and Celsius to the user.
    Uopt = (input('Enter "yes" if you would like to convert another temperature, enter "no" to exit'  ))#Give the user the option of continuing the program or exiting.
    wantout = Uopt.lower()