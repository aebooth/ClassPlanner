/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package core;


import java.util.ArrayList;
import java.io.File;
import java.sql.Timestamp;
import java.io.Serializable;
import java.nio.file.Files;
import java.nio.file.LinkOption;
import java.nio.file.Path;
import java.nio.file.Paths;
/**
 *
 * @author alex
 */
public class Class implements Serializable {
    private String classDirectory;
    private ArrayList<Unit> units;
    private ArrayList<String> notes;
    private String name;
    private ArrayList<String> versions;
    private String currentVersion;
    private ArrayList<File> referenceFiles;
    private ArrayList<File> worksheetFiles;
    private Timestamp lastEdited;
      
    public Class(){
        this(checkDirectoryPath("NewClass"));
    }
      
    public Class(String classDirectory){
        this.classDirectory = classDirectory;
        //TODO: Make this All kinds of file-friendly...
        this.units = new ArrayList<>();
        this.notes = new ArrayList<>();
        this.worksheetFiles = new ArrayList<>();
        this.referenceFiles = new ArrayList<>();
        this.lastEdited = new Timestamp(System.currentTimeMillis());
    }
    
    private static String checkDirectoryPath(String path)
    {
        int n = 1;
        while(Files.exists(Paths.get(path),LinkOption.NOFOLLOW_LINKS)){
            path = path + n;
        }
        return path;
    }
    
    public String getName(){
        return this.name;
    }
    
    public void setName(String name){
        this.name = name;
        updateTimeStamp();
    }
    
    public void addVersion(String version){
        this.versions.add(version);
        updateTimeStamp();
    }
    
    public void removeVersion(int index){
        this.versions.remove(index);
        updateTimeStamp();
    }
    
    public void removeVersion(String version){
        this.versions.remove(version);
        updateTimeStamp();
    }
    
    public void setVersion(String version){
        if(!this.versions.contains(version))
        {
            this.versions.add(version);
        }
            this.currentVersion = version;
            updateTimeStamp();
    }
    
    public String getCurrentVersion(){
        return this.currentVersion;
    }

    public void addUnit(Unit unit){
        this.units.add(unit);
        
    }
    
    public void removeUnit(Unit unit){
        
    }
    
    private void updateTimeStamp()
    {
        this.lastEdited = new Timestamp(System.currentTimeMillis());
    }

}
