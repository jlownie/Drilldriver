import yaml

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

def main():
    # Load activity parameters from a YAML file
    with open(multileveltestfile, "r") as file:
        activityparams = yaml.safe_load(file)

    # Construct an exhaustive set of variable value combinations
    promptvals=getPrompts(activityparams['variables'], 0)

    # Construct prompts from the lists
    None

    # Create a CSV from the generated prompts

if __name__ == "__main__":
    main()