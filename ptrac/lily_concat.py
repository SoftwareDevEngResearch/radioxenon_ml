import sys
import os
import re

ignoreLine = 1;

def checkNumber(number, acceptable_numbers):
  length = len(acceptable_numbers);
  for i in range(0, length):
    if number == acceptable_numbers[i]:
      return True;

  return False;

def writeHead(outFile):

  outFile.write('ID\tNPS\tEnergy1\tEnergy2\n');

def getPrintString(set_id, NPS, energy1, energy2):

  sstring = '' + str(set_id) + '\t' + str(NPS) + '\t' + str(energy1) + '\t' + str(energy2) + '\n';
  return sstring;

def extract_coincidence(in1_data, in2_data, outFile):

  set_id = 0;

  acceptable_npss = [];

  ''' go over all nps that exists in first file '''
  for nps in in1_data.keys():
    ''' check that the specific NPS in file 1 exists in file 2 or not '''
    if nps in in2_data:
      acceptable_npss.append(nps); ''' store the NPS that exists in both files '''
      
  acceptable_npss.sort();  ''' sort based on NPS values '''

  acceptedEventCount = len(acceptable_npss);  ''' extract the number of coincidence NPS '''
  for i in range(0, acceptedEventCount):
    nps = acceptable_npss[i];
    set_id = set_id + 1; ''' increment the ID of coincidence events '''
    outFile.write(getPrintString(set_id, nps, in1_data[nps], in2_data[nps])); ''' print coincidence events based on sorted NPS '''
 
def writeHead_3_in(outFile):

  outFile.write('ID\tNPS\tEnergy1\tEnergy2\tEnergy3\n');

def getPrintString_3_in(set_id, NPS, energy1, energy2, energy3):

  sstring = '' + str(set_id) + '\t' + str(NPS) + '\t' + str(energy1) + '\t' + str(energy2) + '\t' + str(energy3) + '\n';
  return sstring;

def extract_coincidence_3_in(in1_data, in2_data, in3_data, outFile):

  set_id = 0;

  acceptable_npss = [];

  ''' go over all nps that exists in first file '''
  for nps in in1_data.keys():
    ''' check that the specific NPS in file 1 exists in file 2 or not '''
    if nps in in2_data:
      if nps in in3_data:
        acceptable_npss.append(nps); ''' store the NPS that exists in both files '''
      
  acceptable_npss.sort();  ''' sort based on NPS values '''

  acceptedEventCount = len(acceptable_npss);  ''' extract the number of coincidence NPS '''
  for i in range(0, acceptedEventCount):
    nps = acceptable_npss[i];
    set_id = set_id + 1; ''' increment the ID of coincidence events '''
    outFile.write(getPrintString_3_in(set_id, nps, in1_data[nps], in2_data[nps], in3_data[nps])); ''' print coincidence events based on sorted NPS '''
 

def main(args):

  global acceptable_end_reaction_types

  ''' sample code for calling this program: python lily.py 31_Kev_X-ray_Test.txt out.txt '''
  main_adr = os.getcwd();
  adr1 = main_adr + '/' + args[1];  ''' input1 file address'''
  adr2 = main_adr + '/' + args[2];  ''' input2 file address'''
  outAdr = main_adr + '/' + args[3];
  adr3 = main_adr + '/' + args[3];
  contains_3_files = 1;
  try:
    adr3 = outAdr;
    outAdr = main_adr + '/' + args[4];
  except:
    contains_3_files = 0;

  ignoreLine = 1;

  outFile = open(outAdr, 'w');

  writeHead(outFile);

  in1_data = {};
  in2_data = {};
  in3_data = {};
  ignore_counter = 0;


  for line in open(adr1):
    ignore_counter = ignore_counter + 1;
    if ignore_counter > ignoreLine:
      ''' processing the line '''
      line = line.strip(); ''' remove whitespace of the start of each line '''
      line = re.sub("\|", "", line);  ''' remove | signs from the lines '''
      line = re.sub("\t+", " ", line);  ''' remove tabs among the line using regular expression (+ mean it should contain one for sure) '''
      ''' extracting information '''
      particle = line.rstrip().split(' '); ''' this line seprate data that exist in one line and represent them as an array (particle) '''
      NPS = int(particle[1]); ''' extract NPS '''
      in1_data.setdefault(NPS, 0); ''' this line just add NPS type to the dictionary (in1_data) after this line, you 
                                          you can put a value in in1_data[NPS]'''
      in1_data[NPS] = particle[3]; ''' storing energy of NPS in the dictionary (in1_data) '''



  ignore_counter = 0; ''' reset ignore counter '''

  for line in open(adr2):
    ignore_counter = ignore_counter + 1;
    if ignore_counter > ignoreLine:
      ''' processing the line '''
      line = line.strip(); ''' remove whitespace of the start of each line '''
      line = re.sub("\|", "", line);  ''' remove | signs from the lines '''
      line = re.sub("\t+", " ", line);  ''' remove tabs among the line using regular expression (+ mean it should contain one for sure) '''
      ''' extracting information '''
      particle = line.rstrip().split(' '); ''' this line seprate data that exist in one line and represent them as an array (particle) '''
      NPS = int(particle[1]);  ''' extract NPS '''
      in2_data.setdefault(NPS, 0);  ''' this line just add NPS type to the dictionary (in2_data) after this line, you 
                                          you can put a value in in2_data[NPS]'''
      in2_data[NPS] = particle[3]; ''' storing energy of NPS in the dictionary (in2_data) '''



  if contains_3_files == 1:
    ignore_counter = 0; ''' reset ignore counter '''

    for line in open(adr3):
      ignore_counter = ignore_counter + 1;
      if ignore_counter > ignoreLine:
        ''' processing the line '''
        line = line.strip(); ''' remove whitespace of the start of each line '''
        line = re.sub("\|", "", line);  ''' remove | signs from the lines '''
        line = re.sub("\t+", " ", line);  ''' remove tabs among the line using regular expression (+ mean it should contain one for sure) '''
        ''' extracting information '''
        particle = line.rstrip().split(' '); ''' this line seprate data that exist in one line and represent them as an array (particle) '''
        NPS = int(particle[1]);  ''' extract NPS '''
        in3_data.setdefault(NPS, 0);  ''' this line just add NPS type to the dictionary (in2_data) after this line, you 
                                            you can put a value in in2_data[NPS] '''
        in3_data[NPS] = particle[3]; ''' storing energy of NPS in the dictionary (in2_data) '''

  if contains_3_files == 0:
    extract_coincidence(in1_data, in2_data, outFile);  ''' extract and store coincidence events '''
  else:
    extract_coincidence_3_in(in1_data, in2_data, in3_data, outFile);  ''' extract and store coincidence events '''
    
if __name__ == "__main__":
	main(sys.argv)
    
