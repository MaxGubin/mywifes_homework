from __future__ import print_function

NUM_DAYS = 5
HIGH_TEMP_THRESHOLD=90

def get_temps():
  result = []
  for day_number in range(NUM_DAYS):
    print('Enter a temperature for day ', day_number, ':',end=' ')
    result.append(float(input()))
  return result

def find_high_temps(temps):
  return [t for t in temps if t >= HIGH_TEMP_THRESHOLD]

def display_results(high_temps):
  print('Total number of hot days:', len(high_temps))
  print('Your high temperatures for the week:\n', 
      ' '.join((str(t) for t in high_temps)))

def main():
  display_results(find_high_temps(get_temps()))

if __name__ == "__main__":
  main()

