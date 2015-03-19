/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package model;


import java.util.ArrayList;
import java.sql.Timestamp;
import java.io.Serializable;
/**
 *
 * @author alex
 */
public class Course implements Serializable {
    private ArrayList<Unit> units;
    private ArrayList<String> notes;
    private String name;
    private Timestamp lastEdited;
      
    public Course(){
        this("NewClass");
    }
      
    public Course(String classDirectory){
        this.units = new ArrayList<>();
        this.notes = new ArrayList<>();
        this.lastEdited = new Timestamp(System.currentTimeMillis());
    }
    
    public String getName(){
        return this.name;
    }
    
    public void setName(String name){
        this.name = name;
        updateTimeStamp();
    }

    public void addUnit(Unit unit){
        this.units.add(unit);
        updateTimeStamp();
    }
    
    public void removeUnit(Unit unit){
        if(!this.units.remove(unit)){
            System.out.println("No such unit found");
        }
        else updateTimeStamp();
        
    }
    
    private void updateTimeStamp()
    {
        this.lastEdited = new Timestamp(System.currentTimeMillis());
    }

}
