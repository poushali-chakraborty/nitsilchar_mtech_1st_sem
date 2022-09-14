//import java.util.Scanner;
/*
 * demo
 * vertices=5, 
    wMat[][]=
    {{0,3,0,1,0},
    {3, 0, 1, 0, 0},
    {0, 1, 0, 0, 3},
   {1, 0, 0, 0, 7},
    {0,0, 3, 7, 0}}
 */
class Graph{
    int distance[],
    vertices=8, 
    wMat[][]=
    {{0, 2, 5, 7, 0, 0, 0, 0},
    {2, 0, 0, 9, 1, 0, 0, 0},
    {5, 0, 0, 3, 0, 0, 7, 2},
    {7, 9, 3, 0, 10, 0, 0, 5},
    {0, 1, 0, 10, 0, 2, 0, 4},
    {0, 0, 0, 0, 2, 0, 6, 4},
    {0, 0, 7, 0, 0, 6, 0, 8},
    {0, 0, 2, 5, 4, 4, 8, 0}}
    
    ,visited[];
    
    int nill=-1;
    int inft=1000;

    
    Graph(int v){
        //to create a user defined array put the value of v to vertices
        distance=new int[vertices];
        distance[0]=0; //distance from source to source is zero.
        
        visited= new int[vertices];
       
        //wMat=new int[vertices][vertices];
       
       // Scanner sc= new Scanner(System.in);
        for(int i =0;i<vertices;i++){
            //for(int j=0;j<vertices;j++){
            //    System.out.println("if"+(i+1)+"th node & "+(j+1)+"th node are connected put weight otherwise put 0");
            //    wMat[i][j]=sc.nextInt();
                
            //}
            if(i!=0){
                distance[i]=inft; //initially we know nothing about the distance from source to all other nodes
               
            }
            visited[i]=0;// not yet visited

        }


    }
    int mindistance(int ndistance[]){
        /*it is going to return the index of the smallest element in this array, ndistance.
        Ideally it needs to be implemented by priority queue, but to make it simple i am using basic linear approach.  
        */
        //System.out.println("newdistance");
        //for ( int i : ndistance) {
        //    //System.out.print(i+",");
        //}
        int min=inft,index=0;
        for(int i=0;i<vertices;i++){
            
            if(visited[i]==0 && min>ndistance[i]){
                min=ndistance[i];
                index=i;
            }
        }
        //System.out.println("min"+min+","+index);
        return index;

    }
    /*
     * 
     * function dijkstra(G, S)
            for each vertex V in G
                distance[V] <- infinite
                previous[V] <- NULL
                If V != S, add V to Priority Queue Q
            distance[S] <- 0
            
            while Q IS NOT EMPTY
                U <- Extract MIN from Q
                for each unvisited neighbour V of U
                    tempDistance <- distance[U] + edge_weight(U, V)
                    if tempDistance < distance[V]
                        distance[V] <- tempDistance
                        previous[V] <- U
            return distance[], previous[]
     * 
     */
    int[] calculateShortestDistance(){
        
        for(int i=0;i<vertices;i++){
            int u=mindistance(distance);
            
            visited[u]=1; 
            //System.out.println("visited "+u);
            for(int j=0;j<vertices;j++){
                
                if(visited[j]==0 && wMat[u][j]!=0){
                    if(distance[j]>(distance[u]+wMat[u][j])){
                        distance[j]=distance[u]+wMat[u][j];
                    }
                }
            }
            


        }
        return distance;
    }

}
public class dijkastra {
public static void main(String[] args) {
    Graph g= new Graph(5);
    int result[]=g.calculateShortestDistance();
    for (int i : result) {
        System.out.println(i);
    }
}
    
}
