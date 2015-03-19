/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package core;

import java.util.LinkedList;
import java.util.HashMap;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;

/**
 *
 * @author alex
 */
public class Unit {

    private String title;
    private ArrayList<Lesson> lessons;
    private HashMap<ResourceType, ArrayList<String>> resources;
    private final List<String> metaNotes;

    public Unit() {
        this("NewUnit");
    }

    public Unit(String title) {
        this.metaNotes = new ArrayList<>();
        this.lessons = new ArrayList<>();
        for (ResourceType type : ResourceType.values()) {
            resources.put(type, new ArrayList<>());
        }
    }

    public void addResource(String url, String type) {
        try {
            if (!resources.get(ResourceType.valueOf(type)).stream().anyMatch(u -> u.equals(url))) {
                resources.get(ResourceType.valueOf(type)).add(url);
            }
        } catch (IllegalArgumentException e) {
            System.out.println(type + " is not a valid resource type.");
        }

    }

    public void removeResource(String url) {
        resources.forEach((k, v) -> v.remove(url));
    }

    public List<String> currentResources() {
        LinkedList<String> urls = new LinkedList<>();
        resources.forEach((k, v) -> urls.addAll(v));
        return urls;
    }

    public List<String> missingResourceTypes() {
        LinkedList<String> types = new LinkedList<>();
        for (Map.Entry pair : this.resources.entrySet()) {
            if (((List<String>) pair.getValue()).isEmpty()) {
                types.add(((ResourceType) pair.getKey()).toString());
            }
        }
        return types;
    }
    
    private void addLesson(Lesson lesson){
        if(!this.lessons.contains(lesson)){
            this.lessons.add(lesson);
        }
        else System.out.println("lesson already exists within the unit!");
    }
    

    public String getTitle() {
        return this.title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public void makeNote(String note) {
        metaNotes.add(note);
    }

    public void scratchNote(int index) {
        if (index < metaNotes.size() && index >= 0) {
            metaNotes.remove(index);
        } else {
            System.out.println(index + " is an invalid index");
        }
    }

    private enum ResourceType {

        PRETEST,
        UNIT_CALENDAR,
        POSTTEST
    }
}
