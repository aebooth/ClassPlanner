package core;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;

public class Lesson{

private static long numLessons = 0;
private long id;
private String title;
private final Map<ResourceType,List<String>> resources;
private final List<String> metaNotes;


public Lesson(String title){
   this.title = title;
   resources = new HashMap<>();
   
   metaNotes = new ArrayList<>();
   
   for(ResourceType type:ResourceType.values()){
      resources.put(type,new LinkedList<>());
   }
   
   this.id = numLessons;
   numLessons++;
}

public void add(String url, String type){
   try{
   if(!resources.get(ResourceType.valueOf(type)).stream().anyMatch(u -> u.equals(url)))
           resources.get(ResourceType.valueOf(type)).add(url);
}
catch(IllegalArgumentException e){
    System.out.println(type + " is not a valid resource type.");
}
    
}

public void remove(String url){
   resources.forEach((k,v)->v.remove(url));
}

public List<String> currentResources(){
   LinkedList<String> urls = new LinkedList<>();
   resources.forEach((k,v)->urls.addAll(v));
   return urls;
}

public List<String> missingResourceTypes(){
   LinkedList<String> types = new LinkedList<>();
   for(Map.Entry pair:this.resources.entrySet())
       if(((List<String>)pair.getValue()).isEmpty())
           types.add(((ResourceType)pair.getKey()).toString());
   return types;
}

public String getTitle(){
    return this.title;
}

public void setTitle(String title){
   this.title = title;
}

public void makeNote(String note){
   metaNotes.add(note);
}

public void scratchNote(int index){
   if(index < metaNotes.size() && index >= 0){
      metaNotes.remove(index);
   }
   else System.out.println(index + " is an invalid index");
}

private enum ResourceType{
   WARM_UP,
   TEACHER_NOTE,
   STUDENT_NOTE,
   PLAN,
   HW_ASSIGNMENT,
   HW_KEY,
   HW_AID,
   PRESENTATION,
   QUIZ,
   DEMO,
   LAB_SHEET;
}

}

