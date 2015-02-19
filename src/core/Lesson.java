public class Lesson{

private static long int numLessons = 0;
private long int id;
private String title;
private Map<ResourceType,List<URL>> resources;
private List<String> metaNotes;


public Lesson(String title)
   this.title = title;
   resources = new HashMap<>();
   
   metaNotes = new ArrayList<>();
   
   for(ResourceType type:ResourceType.values()){
      resources.add(type,new LinkedList<>());
   }
   
   this.id = numLessons;
   numLessons++;
}

public void add(URL url, ResourceType type){
   resources.add(type, url);
}

public void remove(URL url){
   resources.forEach((k,v)->if(v.contains(url)){v.removeFirst(url)});
}

public List<URL> currentResources(){
   LinkedList<URL> urls = new LinkedList<>();
   resources.forEach((k,v)->urls.addAll(v));
   return urls;
}

public List<ResourceType> missingResourceTypes(){
   LinkedList<ResourceType> types = new LinkedList<>();
   resources.forEach((k,v)->if(v.size() == 0){types.add(k)});
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

