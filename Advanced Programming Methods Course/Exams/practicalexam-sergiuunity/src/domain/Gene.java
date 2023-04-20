package domain;

public class Gene implements Comparable<Gene> {


    private String name;
    private String organism;
    private String function;
    private String sequence;

    public Gene(String name, String organism, String function, String sequence) {
        this.name = name;
        this.organism = organism;
        this.function = function;
        this.sequence = sequence;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getOrganism() {
        return organism;
    }

    public void setOrganism(String organism) {
        this.organism = organism;
    }

    public String getFunction() {
        return function;
    }

    public void setFunction(String function) {
        this.function = function;
    }

    public String getSequence() {
        return sequence;
    }

    public void setSequence(String sequence) {
        this.sequence = sequence;
    }

    @Override
    public String toString() {
        return name + "  |  " + organism + "  |  " + function;
    }

    @Override
    public int compareTo(Gene o) {
        return organism.compareTo(o.getOrganism());
    }

    public boolean isGood(String currentText, String selectedOption)
    {
        if(currentText.equals("") || selectedOption.equals("All"))
            return true;
        if(getOrganism().equals(selectedOption))
            if(name.contains(currentText) || function.contains(currentText))
                return true;
        return false;
    }

}
