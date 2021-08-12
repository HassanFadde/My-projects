import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner input=new Scanner((System.in));
        String liste_services[]={
                "modifier un ligne dans votre bloc note",
                "modifier le mot de passe",
                "modifier le nom d'utilisateur",
                "suprimmer un ligne dans votre bloc note",
                "ecrire au fichier",
                "lire le fichier",
                "savoir le nom d'utilisateur",
                "savoir le nom du fichier",
                "peut lire le fichier",
                "peut ecrire à ce fichier",
                "la taille de ce fichier",
                "nombre du lignes de ce fichier",
                "absolute path de ce fichier",
                "arreter le programme"};
        int i=1;
        String user_name,name_file,password;
        NoteBook note_book = null;
        boolean fichier_est_disponible=false;
        int choix;
        while(!fichier_est_disponible){
            System.out.println("------------------------------------------------------------------------------------------------------------------------");
            System.out.println("1.creer un nouveau bloc note\n2.ouvrir votre bloc note\n3.cripter un fichier\n4.decripter un fichier\n5.arreter le programme");
            System.out.println("------------------------------------------------------------------------------------------------------------------------");
            System.out.print("entrer votre choix : ");
            choix=input.nextInt();
            if (choix==1){
                System.out.print("entrer votre nom : ");
                user_name=input.nextLine();
                user_name=input.nextLine();
                System.out.print("entrer un nom pour votre bloc note : ");
                name_file=input.nextLine();
                System.out.print("entrer un mot de passe pour votre bloc note : ");
                password=input.nextLine();
                note_book=new NoteBook(user_name,name_file,password);
                if(note_book.get_file_size()!=""){
                    fichier_est_disponible=true;
                }
            }
            else if(choix==2){
                System.out.print("entrer le nom du votre bloc note : ");
                name_file=input.nextLine();
                name_file=input.nextLine();
                System.out.print("entrer le mot de passe de votre bloc note : ");
                password=input.nextLine();
                note_book=new NoteBook(name_file,password);
                if(note_book.get_file_size()!=""){
                    fichier_est_disponible=true;
                }
                System.out.println("bonjour "+note_book.get_name_user()+".");
            }
            else if(choix==3){
                System.out.print("entrer votre nom : ");
                user_name=input.nextLine();
                user_name=input.nextLine();
                System.out.print("entrer le path du votre fichier : ");
                String path_name=input.nextLine();
                System.out.print("entrer votre mot de passe : ");
                password=input.nextLine();
                note_book=new NoteBook(user_name,path_name,password,true);
            }
            else if(choix==4){
                System.out.print("entrer le path du votre fichier : ");
                String path_name=input.nextLine();
                path_name=input.nextLine();
                System.out.print("entrer votre mot de passe : ");
                password=input.nextLine();
                note_book=new NoteBook(path_name,password,true);
            }
            else{
                System.out.print("le programme va s'arreter !!");
                return;
            }

        }
        do{
            System.out.println("------------------------------------------------------------------------------------------------------------------------");
            for(String service:liste_services){
                if (service==null){
                    continue;
                }
                System.out.println(i+"."+service);
                i++; }
            System.out.println("------------------------------------------------------------------------------------------------------------------------");
            i=1;
            System.out.print("choisir votre choix : ");
            choix=input.nextInt();
            switch(choix){
                case 1:
                    note_book.read_file(true);
                    System.out.print("choisir la ligne que vous voulez la modifier : ");
                    int num_ligne=input.nextInt();
                    System.out.print("par quoi vous voulez le modifier : ");
                    String nouveau_ligne=input.nextLine();
                    nouveau_ligne=input.nextLine();
                    if (nouveau_ligne.length()==0){
                        System.out.println("si vous voulez suprimmer une ligne entrer 4");
                    }else{
                        note_book.update_line(num_ligne,nouveau_ligne);
                    }
                    break;
                case 2:
                    System.out.print("entrer votre mot de passe : ");
                    String mot_de_passe=input.nextLine();
                    mot_de_passe=input.nextLine();
                    System.out.print("entrer votre nouveau mot de passe : ");
                    String nouveau_mot_de_passe=input.nextLine();
                    if (nouveau_mot_de_passe.length()==0){
                        System.out.println("la langueure du mot de passe faut etre plus que 0 !!");
                    }else if(mot_de_passe.equals(nouveau_mot_de_passe)) {
                        System.out.println("le nouveau mot de passe faut étre different que l'actuelle");
                    }else{
                        note_book.update_password(mot_de_passe,nouveau_mot_de_passe);
                    }
                    break;
                case 3:
                    System.out.print("entrer votre nouveau nom : ");
                    String nouveau_nom=input.nextLine();
                    nouveau_nom=input.nextLine();
                    if(nouveau_nom.length()==0){
                        System.out.println("la langueure du votre nouveau nom faut étre diffirent que 0");
                    }else if(nouveau_nom.equals(note_book.get_name_user())){
                        System.out.println("le nouveau nom faut étre diffirent que l'actuelle");
                    }else{
                        note_book.update_user_name(nouveau_nom);
                    }
                    break;
                case 4:
                    note_book.read_file(true);
                    System.out.print("choisir la ligne que vous voulez la suprimmer : ");
                    num_ligne=input.nextInt();
                    note_book.delete_line(num_ligne);
                    break;
                case 5:
                    System.out.println("ecrivez votre texte à ajouter au fichier si vous voulez souter la ligne click entrer et si vous voulez arreter d'ecrire click dans une ligne vide entrer");
                    String ligne;
                    ligne=input.nextLine();
                    do{
                        System.out.print("ecrire votre ligne ici : ");
                        ligne=input.nextLine();
                        if(ligne.length()!=0){
                            note_book.write_in_file(ligne);
                        }
                    }while(ligne.length()!=0);
                    System.out.println("vous allez arreter d'ecrire");
                    break;
                case 6:
                    note_book.read_file(false);
                    if (note_book.getNum_lines()==0){
                        System.out.println("votre fichier est vide");
                    }
                    System.out.print("click entrer pour continue ...");
                    input.nextLine();
                    input.nextLine();
                    break;
                case 7:
                    System.out.println(note_book.get_name_user());
                    System.out.print("click entrer pour continue ...");
                    input.nextLine();
                    input.nextLine();
                    break;
                case 8:
                    System.out.println(note_book.get_name_file());
                    System.out.print("click entrer pour continue ...");
                    input.nextLine();
                    input.nextLine();
                    break;
                case 9:
                    System.out.println(note_book.can_read());
                    System.out.print("click entrer pour continue ...");
                    input.nextLine();
                    input.nextLine();
                    break;
                case 10:
                    System.out.println(note_book.can_write());
                    System.out.print("click entrer pour continue ...");
                    input.nextLine();
                    input.nextLine();
                    break;
                case 11:
                    System.out.println(note_book.get_file_size());
                    System.out.print("click entrer pour continue ...");
                    input.nextLine();
                    input.nextLine();
                    break;
                case 12:
                    System.out.println("nombres du ligne : "+note_book.getNum_lines());
                    System.out.print("click entrer pour continue ...");
                    input.nextLine();
                    input.nextLine();
                    break;
                case 13:
                    System.out.println(note_book.get_absolute_path());
                    System.out.print("click entrer pour continue ...");
                    input.nextLine();
                    input.nextLine();
                    break;
                default:
                    System.out.println("le programe va s'arreter !!");
                    break;
            }
        }while(choix>=1&&choix<=13);
    }
}
