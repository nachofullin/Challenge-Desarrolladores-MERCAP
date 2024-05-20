from datetime import datetime       #Attributes: year, month, day, hour, minute, second, microsecond, and tzinfo.

class Call:
    def __init__(self, date_time, duration, category, destination = None):
        self.date_time = date_time          #date and time of call
        self.duration = duration            #in minutes
        self.category = category            #'local', 'national' or 'international'
        self.destination = destination      #for international and national calls

class Bill:
    def __init__(self, month, monthly_fee):
        self.month = month          #month of the bill
        self.monthly_fee = monthly_fee      #total fee to pay
        self.calls = []             #list of calls in that month

    def add_call(self, call):
        self.calls.append(call)

    def calculate_total(self):
        total = self.monthly_fee
        for call in self.calls:
            total += self.calculate_individual_call(call)
        return total
    
    def calculate_individual_call(self, call):
        cost = 0
        if call.category == 'local':
                cost = self.calculate_local_cost(call)
        elif call.category == 'national':
                cost = self.calculate_national_cost(call)
        elif call.category == 'international':
                cost = self.calculate_international_cost(call)
        return cost

    def calculate_local_cost(self, call):
        fee = 0
        day = call.date_time.weekday()
        hour = call.date_time.hour
        if day <= 4:    #Monday to Friday
            if 8 <= hour < 20:
                fee = call.duration * 0.20
            else:
                fee = call.duration * 0.10
        else:       #Saturday and Sunday
            fee = call.duration * 0.10      #Could be simplified in just one if since 0.10 is repeated but kept it the way it was stated in the instructions for posible changes in fees
        return fee

    def calculate_national_cost(self, call):
        #example list of fees for each locality
        national_rates = {
            'locality1' : 0.20,
            'locality2' : 0.15,
            'locality3' : 0.30,
        }
        fee = national_rates[call.destination] * call.duration
        return fee

    def calculate_international_cost(self, call):
        #example list of fees for each locality
        international_rates = {
            'country1' : 2.00,
            'country2' : 1.15,
            'country3' : 1.30,
        }
        fee = international_rates[call.destination] * call.duration
        return fee

    def print_bill(self):
        print(f'{self.month} bill')
        print(f'Monthly fee: {self.monthly_fee}')
        print(f'Call list:')
        total_payment = self.calculate_total()
        for index, call in enumerate(self.calls, start=1):
            print(f'{index}. Date: {call.date_time}, Duration: {call.duration}, Category: {call.category}, Destination: {call.destination}, Cost: {round(self.calculate_individual_call(call), 2)}')
        print(f'Total amount to pay: {round(total_payment, 2)}')

# Example
phone_bill = Bill('May', 15.00)
phone_bill.calls.append(Call(datetime(2024, 5, 17, 12, 00), 15, 'local'))
phone_bill.calls.append(Call(datetime(2024, 5, 18, 18, 30), 5, 'local'))
phone_bill.calls.append(Call(datetime(2024, 5, 16, 7, 10), 30, 'national', 'locality1'))
phone_bill.calls.append(Call(datetime(2024, 5, 15, 15, 40), 21, 'national', 'locality3'))
phone_bill.calls.append(Call(datetime(2024, 5, 11, 3, 00), 45, 'international', 'country2'))

phone_bill.print_bill()