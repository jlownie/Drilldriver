import yaml
import argparse

keysfile="Drills/Keys.yml"
multileveltestfile="Tests/3lvltest.yml"

def getPrompts( variables, myindex ):
    # If we are the last in the set of variable values, just return those values
    if myindex == len(variables)-1:
        return variables[myindex]['values']
    else:
        # Get all remaining values
        deeperprompts=getPrompts(variables, myindex+1)

        # Combine them with our values
        myprompts=[]
        for myval in variables[myindex]['values']:
            for deeperprompt in deeperprompts:
                newprompt=[myval]
                if isinstance(deeperprompt, list):
                    newprompt += deeperprompt
                else:
                    newprompt.append(deeperprompt)                
                myprompts.append(newprompt)
        return myprompts

# Parses command line parameters and returns them
def parseArgs():
  parser = argparse.ArgumentParser(
      prog='Drilldriver',
      description='Software for practicing drills of various kinds.')
  #parser.add_argument('pdfname', help="The path to the PDF file to be converted")
  parser.add_argument('Inputfile', help="The activity parameters file")
  return parser.parse_args()

def main():
    args=parseArgs()    

    # Load activity parameters from a YAML file
    with open(args.Inputfile, "r") as file:
        activityparams = yaml.safe_load(file)

    # Construct an exhaustive set of variable value combinations
    promptvals=getPrompts(activityparams['prompt_variables'], 0)

    # Construct prompts from the lists
    promptstrs=[]
    promptformat=activityparams['prompt_format']
    for thisval in promptvals:
        thisstr=promptformat.format(*thisval)
        promptstrs.append(thisstr)

    # Create a CSV from the generated prompts
    None

if __name__ == "__main__":
    main()