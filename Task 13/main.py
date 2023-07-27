from datetime import datetime, timedelta

def friday_13_months(year):
	"""Returns the tuple of months that have a Friday the 13th in the given year. The months show up in order."""
  
	current_date = datetime(year, 1, 1) #Set starting date as January 1st of the given year
  
	end_date = datetime(year+1, 1, 1) #Set end date as January 1st of the following year
  
	friday_13_tuple = () #Store months with Friday the 13th
  
	while current_date < end_date:
    
		if current_date.strftime("%d") == "13" and current_date.weekday()==4: #Checks to see if the current date is a Friday the 13th
      
			friday_13_tuple = friday_13_tuple + (current_date.strftime("%B"),) #If true, adds month to the tuple of Friday the 13th months
      
		current_date+=timedelta(1) #goes to next day
    
	return friday_13_tuple
