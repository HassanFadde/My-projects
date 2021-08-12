import java.io.*;
import java.util.Scanner;
public class NoteBook {
    private String password;
    private int num_lines;
    private int cle;
    private File note_book;
    private boolean password_is_correct=true;
    private String user_name;
    private boolean private_line=true;
    private File names_files=new File("names files.txt");
    protected NoteBook(String name_user,String name_file,String password){
        this.note_book=new File(name_file+".txt");
        this.password=password;
        this.user_name=name_user;
        this.cle=(user_name.length()*999)%8+1;
        try {
            this.names_files.createNewFile();
            if (this.note_book.createNewFile()){
                System.out.println("file created");
                System.out.println("name file : "+this.note_book.getName());
                System.out.println("absolute path : "+this.note_book.getAbsolutePath());
                FileWriter write_cle_and_password=new FileWriter(this.note_book.getAbsolutePath(),true);
                write_cle_and_password.write((char)(cle+1)+"\n");
                write_cle_and_password.write(cripter(this.password)+"\n");
                write_cle_and_password.write(cripter(this.user_name)+"\n");
                write_cle_and_password.close();
                if (!name_file_is_find(name_file)){
                FileWriter add_name_file=new FileWriter(this.names_files.getAbsolutePath(),true);
                add_name_file.write(name_file+"\n");
                add_name_file.close();}
                this.num_lines=3;
                this.password_is_correct=true;
            }
            else{
                this.password_is_correct=false;
                throw (new Exception("file repeted !!"));
            }
        } catch (IOException e) {
            e.printStackTrace();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
    protected NoteBook(String name_file, String password){
        try{
             if (!name_file_is_find(name_file)){
                 this.password_is_correct=false;
                 throw (new Exception("file not find !!"));
             }
            this.password_is_correct=true;
             this.note_book=new File(name_file+".txt");
             this.note_book.createNewFile();
             Scanner read_cle_and_password=new Scanner(this.note_book);
             this.cle=(int)read_cle_and_password.nextLine().toCharArray()[0]-1;
             this.password=decripter(read_cle_and_password.nextLine());
             if(!verificateur(password)){
                 this.password_is_correct=false;
                 throw (new Exception("password incorrect!!"));
             }
            this.user_name=decripter(read_cle_and_password.next());
             read_cle_and_password.close();
             Scanner num_lines=new Scanner(this.note_book);
             while(num_lines.hasNextLine()){
                 num_lines.nextLine();
                 this.num_lines++;
             }
             num_lines.close();
        }catch(Exception e){
            e.printStackTrace();
        }
    }
    protected NoteBook(String user_name,String path_name,String password,boolean in_this_file){
        try{
            this.note_book=new File(path_name);
            if(!this.note_book.exists()){
                throw (new Exception("file not find !!"));
            }
            this.note_book.createNewFile();
            Scanner read_file=new Scanner(this.note_book);
            int num_lines=0;
            while(read_file.hasNextLine()){
                num_lines++;
                read_file.nextLine();
            }
            read_file.close();
            String lines []=new String[num_lines];
            Scanner read_lines=new Scanner(this.note_book);
            int i=0;
            while(read_lines.hasNextLine()){
                lines[i]=read_lines.nextLine();
                i++;
            }
            read_lines.close();
            this.cle=(user_name.length()*999)%8+1;
            FileWriter write_in_file=new FileWriter(this.note_book);
            write_in_file.write("detpirc\n");
            write_in_file.write((char)(this.cle+1)+"\n");
            write_in_file.write(cripter(password)+"\n");
            write_in_file.write(num_lines+"\n");
            write_in_file.close();
            FileWriter write_lines=new FileWriter(this.note_book,true);
            for(String line : lines){
                write_lines.write(cripter(line)+"\n");
            }
            write_lines.close();
        } catch (IOException e) {
            e.printStackTrace();
        }catch(Exception e){
            e.printStackTrace();
        }
    }
    protected NoteBook(String path_name,String password,boolean in_this_file){
        try {
            this.note_book = new File(path_name);
            if (!this.note_book.exists()){
                throw (new Exception("file not find !!"));
            }
            this.note_book.createNewFile();
            Scanner read_file=new Scanner(this.note_book);
            if(!read_file.hasNextLine()){
                return;
            }
            if (!read_file.nextLine().equals("detpirc")){
                throw(new Exception("this file note cripted"));
            }
            this.cle=(int)read_file.nextLine().toCharArray()[0]-1;
            this.password=decripter(read_file.nextLine());
            if(!this.password.equals(password)){
                throw (new Exception("password is incorrect !!"));
            }
            int num_lines=read_file.nextInt();
            int i=0;
            String[] lines=new String[num_lines];
            while(read_file.hasNextLine()){
                lines[i]=read_file.nextLine();
                if (!lines[i].equals("")){
                i++;}
            }
            read_file.close();
            FileWriter write_lines=new FileWriter(this.note_book);
            for(String line:lines){
                if(line==null){
                    continue;
                }
                write_lines.write(decripter(line)+"\n");
            }
            write_lines.close();
        }catch(IOException e){
            e.printStackTrace();
        }catch(Exception e){
            e.printStackTrace();
        }
    }
    protected void delete_line(int num_line){
        num_line+=3;
        try{
            if (this.num_lines<num_line){
                throw (new Exception("line not find !!"));
            }
            if (!this.password_is_correct){
                throw (new Exception("Error"));
            }
            if (num_line>=1 && num_line<=3 ){
                throw (new Exception("this lines is privates"));
            }
            num_line--;
            String lines []=new String[this.num_lines];
            Scanner update=new Scanner(this.note_book);
            int i=0;
            while (update.hasNextLine()){
                if(i==this.num_lines){
                    break;
                }
                if(i==num_line){
                    update.nextLine();
                }else{
                    lines[i]=update.nextLine();
                }
                i++;
            }
            update.close();
            FileWriter update_file=new FileWriter(this.note_book);
            for (String line:lines){
                if(line==null){
                    continue;
                }
                update_file.write(line+"\n");
            }
            update_file.close();
            this.num_lines--;
            System.out.println("la ligne "+(num_line-2)+" a été suprimmer");
        }catch(Exception e){
            e.printStackTrace();
        }
    }
    protected void update_line(int num_line,String new_line){
        num_line+=3;
        try{
            if (!this.password_is_correct){
                throw (new Exception("Error"));
            }
            if (this.num_lines<num_line){
                throw (new Exception("line not find !!"));
            }
            if (num_line>=1 && num_line<=3&&this.private_line ){
                this.private_line=true;
                throw (new Exception("this lines is privates"));
            }
            num_line--;
            String lines []=new String[this.num_lines];
            Scanner update=new Scanner(this.note_book);
            int i=0;
            while (update.hasNextLine()){
                if(i==this.num_lines){
                    break;
                }
                if(i==num_line){
                    lines[i]=cripter(new_line);
                    update.nextLine();
                }else{
                    lines[i]=update.nextLine();
                }
                i++;
            }
            update.close();
            FileWriter update_file=new FileWriter(this.note_book);
            for (String line:lines){
                if (line==null)
                    continue;
                update_file.write(line+"\n");
            }
            update_file.close();
            if (num_line==1){
                System.out.println("votre mot de passe a été modifier.");
            }else{
                System.out.println("la line "+(num_line-2)+" a été modifier.");
            }
        }catch(Exception e){
            e.printStackTrace();
        }
    }
    protected void update_password(String last_password,String new_password) {
        if (last_password.equals(this.password)) {
            if (this.password_is_correct){
            this.password = new_password;
            }
            this.private_line=false;
           update_line(-1,this.password);
        }
        else {
        System.out.println("your password is incorrect !!");}
    }
    protected  void write_in_file(String text){
       try{
           if (!this.password_is_correct){
               throw (new Exception("Error"));
           }
           FileWriter write_in_file=new FileWriter(this.note_book.getAbsolutePath(),true);
           write_in_file.write(cripter(text)+"\n");
           write_in_file.close();
           this.num_lines+=1;
       }catch(Exception e){
           e.printStackTrace();
       }
    }
    protected void  read_file(boolean with_num_lines){
        try{
            if (!this.password_is_correct){
                throw (new Exception("Error"));
            }
            Scanner read_lines=new Scanner(this.note_book);
            int in_line=0;
            while(read_lines.hasNext()){
                in_line+=1;
                if (in_line<=2){
                    read_lines.next();
                    continue;
                }
                String line=decripter(read_lines.next());
                if (in_line==3){
                    System.out.println("File of : "+line);
                    continue;
                }
                if (with_num_lines){
                System.out.println(in_line-3+" . "+line);}else{
                    System.out.println(line);
                }
            }
        }catch(Exception e){
            e.printStackTrace();
        }
    }
    protected String get_absolute_path(){
        try{
            if(!password_is_correct){
                throw (new Exception("Error"));
            }
        }catch(Exception e){
            e.printStackTrace();
        }
        return "absolute path : "+this.note_book.getAbsolutePath();
    }
    protected  String get_name_file() {
        try {
            if (!password_is_correct) {
                throw (new Exception("Error"));
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        return "name file : "+this.note_book.getName();
    }
    protected String get_name_user(){
        try {
            if (!password_is_correct) {
                throw (new Exception("Error"));
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        return this.user_name;
    }
    protected  String can_read() {
        try {
            if (!password_is_correct) {
                throw (new Exception("Error"));
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        return "can read : "+this.note_book.canRead();
    }
    protected  String can_write() {
        try {
            if (!password_is_correct) {
                throw (new Exception("Error"));
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        return "can write : "+this.note_book.canWrite();
    }
    protected  String get_file_size() {
        try {
            if (!password_is_correct) {
                throw (new Exception("Error"));
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        return "size : "+this.note_book.length()+"bytes";
    }
    protected int getNum_lines(){
        try {
            if (!password_is_correct) {
                throw (new Exception("Error"));
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        return this.num_lines;
    }
    protected void update_user_name(String new_name){
        try {
            if (!password_is_correct) {
                throw (new Exception("Error"));
            }
            this.user_name=new_name;
            String lines []=new String[this.num_lines];
            Scanner update=new Scanner(this.note_book);
            int i=0;
            while (update.hasNextLine()){
                if(i==this.num_lines){
                    break;
                }
                lines[i]=decripter(update.nextLine());
                i++;
            }
            update.close();
            i=0;
            this.cle=(this.user_name.length()*999)%8+1;
            FileWriter update_file=new FileWriter(this.note_book);
            for (String line:lines){
                i++;
                if (line==null)
                    continue;
                if (i==1){
                    update_file.write((char)(this.cle+1)+"\n");
                    continue;
                }
                if(i==3){
                    update_file.write(cripter(this.user_name)+"\n");
                    continue;
                }
                update_file.write(cripter(line)+"\n");
            }
            update_file.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
    private String cripter(String string){
        if (string==null){
            return "\n";
        }
        char[] chars=string.toCharArray();
        char [] new_chars = new char[chars.length];
        int i=0;
        for (char element:chars) {
            int new_element=element;
            new_chars [i]=(char)(new_element+this.cle);
            i++;
        }
        return new String(new_chars);
    }
    private String decripter(String string){
        if (string==null){
            return "\n";
        }
        char[] chars=string.toCharArray();
        char [] new_chars = new char[chars.length];
        int i=0;
        for (char element:chars) {
            int new_element=element;
            new_chars [i]=(char)(new_element-this.cle);
            i++;
        }
        return new String(new_chars);
    }
    private boolean verificateur(String password){
        return this.password.equals(password);
    }
    private boolean name_file_is_find(String name_file){
        try{
            Scanner read_names_files= new Scanner(this.names_files);
            while(read_names_files.hasNextLine()){
                if (name_file.equals(read_names_files.nextLine())){
                    return true;
                }
            }
        }catch(Exception e){
            e.printStackTrace();
        }
        return false;
    }
}
