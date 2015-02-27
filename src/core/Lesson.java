package core;

import java.net.URL;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;
import java.util.Map;

public class Lesson{

private static long numLessons = 0;
private long id;
private String title;
private Map<ResourceType,List<URL>> resources;
private List<String> metaNotes;


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

public void add(URL url, ResourceType type){
   if(!resources.get(type).stream().anyMatch(u -> u.equals(url)))
           resources.get(type).add(url);
}

public void remove(URL url){
   resources.forEach((k,v)->v.remove(url));
}

public List<URL> currentResources(){
   LinkedList<URL> urls = new LinkedList<>();
   resources.forEach((k,v)->urls.addAll(v));
   return urls;
}

public List<ResourceType> missingResourceTypes(){
   LinkedList<ResourceType> types = new LinkedList<>();
   for(Map.Entry pair:this.resources.entrySet())
       if(((List<URL>)pair.getValue()).isEmpty())
           types.add((ResourceType)pair.getKey());
   return types;
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
   else throw new IllegalArgumentException("Scratch failed: That index dos not point to a note!");
}


}

