/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package core;


import java.util.ArrayList;
import java.io.File;
import java.time.Instant;
import java.io.Serializable;
/**
 *
 * @author alex
 */
public class Class implements Serializable {
    private ArrayList<Unit> units;
    private ArrayList<String> notes;
    private String name;
    private ArrayList<String> versions;
    private String currentVersion;
    private ArrayList<File> referenceFiles;
    private ArrayList<File> worksheetFiles;
    private Instant lastEdited;
    
    public Class(){
        this.units = new ArrayList<Unit>();
        this.notes = new ArrayList<String>();
        this.worksheetFiles = new ArrayList<File>();
        this.referenceFiles = new ArrayList<File>();
    }
    
    public String getName(){
        return this.name;
    }
    
    public void setName(String name){
        this.name = name;
    }
    
    public void addVersion(String version){
        this.versions.add(version);
    }
    
    public void removeVersion(int index){
        this.versions.remove(index);
    }
    
    public void removeVersion(String version){
        this.versions.remove(version);
    }
    
    public void setVersion(String version){
        if(!this.versions.contains(version))
        {
            this.versions.add(version);
        }
            this.currentVersion = version;
    }
    
    public String getCurrentVersion(){
        return this.currentVersion;
    }

}
