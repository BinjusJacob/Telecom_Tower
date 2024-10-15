from django.shortcuts import render, redirect
from .models import *
import os
import pandas as pd
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request,'home.html')

def dashboard(request):
    obj = Tower.objects.all()
    context = {"obj":obj}
    return render(request,'dashboard.html',context)

def data(request):
    return render(request,'data.html')

def detailedview(request, id):
    # Retrieve the Tower object based on the provided id
    obj = Tower.objects.get(id=id)
    
    if not obj.file:
        # If no file is uploaded, return an error message
        return HttpResponse("No data file uploaded for this tower.", status=404)

    # Handle POST request for updating the Tower object
    if request.method == "POST":
        name = request.POST.get('name')
        location = request.POST.get('location')
        file=request.POST.get('file')
        obj.name = name
        obj.location = location
        obj.file=file 
        obj.save()
        return redirect('home')  # Redirect to the home page after update

    # Load the data from an Excel file
    # file_path = os.path.join('C:\\Users\\User\\Desktop\\Codeme\\TelecomTower\\Tower_app\\my_project\\my_app\\', 'Data.xlsx')
    # df = pd.read_excel(file_path)
    try:
        # Load the data from the uploaded Excel file
        df = pd.read_excel(obj.file.path)  # Use .path to get the file's full path

        # Ensure that the DataFrame has columns for charts
        df.columns = df.columns.str.strip()  # Strip any whitespace from column names
        if 'TIME' in df.columns:
            df['TIME'] = df['TIME'].astype(str)
        else:
            return HttpResponse("The 'TIME' column was not found in the Excel file.", status=404)

        # Extract columns from the dataframe and pass them to the template
        context = {
            'obj': obj,  # Pass the Tower object to the template
            'time': df['TIME'].tolist(),
            'sensor_status': df['SENSOR Status'].tolist(),
            'cabin_door_status': df['CABIN DOOR status'].tolist(),
            'clean_duct_status': df['CLEAN DUCT Status'].tolist(),
            'generator_status': df['Generator_status'].tolist(),
            'fuel_cap_status': df['FUEL CAP status'].tolist(),
            'fuel_liters': df['FUEL Ltr'].tolist(),
        }

        return render(request, 'dashboard_detailed_page.html', context)

    except FileNotFoundError:
        # If the file path does not exist, return an error message
        return HttpResponse("The file for this tower could not be found.", status=404)

    except Exception as e:
        # Catch any other exceptions and return a generic error message
        return HttpResponse(f"An error occurred: {str(e)}", status=500)