using System.Windows;
using System.Windows.Controls;
using System.IO;
using System.Diagnostics;

namespace autoViewer
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        /*Fields*/
        string wanted_scripts = "None";
        string root_directory = "None";

        public MainWindow ()
        {
            InitializeComponent();

            foreach (string s in File.ReadLines("config.txt"))
            {
                root_directory = s;
            }

            // get files under root directory
            RenewScripts();
        }

        private void RenewScripts()
        {
            ListBox_ListScripts.Items.Clear();
            var files = Directory.EnumerateFiles(root_directory, "auto*.txt");
            foreach (string file in files)
            {
                ListBox_ListScripts.Items.Add(file.Substring(root_directory.Length));
            }
        }

        private void ListBox_ListScripts_SelectionChanged (object sender, SelectionChangedEventArgs e)
        {
            this.wanted_scripts = ListBox_ListScripts.SelectedItem.ToString();
            RenewScripts();
        }

        private void BtnReadScript_Click (object sender, RoutedEventArgs e)
        {
            if (this.wanted_scripts == "None")
            {
                StatusBar_mainStatus.Items.Clear();
                StatusBar_mainStatus.Items.Add("No selected script.");
            }
            else
            {   // open controller
                string script = this.root_directory + this.wanted_scripts,
                       controller = this.root_directory + "autoController.py", output, error;
                
                Process p = new Process();

                p.StartInfo.FileName = "python.exe";
                p.StartInfo.Arguments = controller + ' ' + script;
                p.StartInfo.RedirectStandardError = true;
                p.StartInfo.RedirectStandardOutput = true;

                p.Start();

                output = p.StandardOutput.ReadToEnd();
                error = p.StandardError.ReadToEnd();

                txtBoxShow_Stdout.Text = output;
                txtBlock_Stderr.Text = error;
            }
        }

        private void BtnClose_Click (object sender, RoutedEventArgs e)
        {
            this.Close();
        }

        private void Btn_editScript_Click (object sender, RoutedEventArgs e)
        {
            Process p = new Process();
            try
            {
                p.StartInfo.FileName = "explorer.exe";
                p.StartInfo.Arguments = this.root_directory;
                p.Start();
                p.WaitForExit();
            }
            catch (System.ComponentModel.Win32Exception ex)
            {
                StatusBar_mainStatus.Items.Clear();
                StatusBar_mainStatus.Items.Add($"{ex.Message}");
            }
            
        }

        private void Btn_Help_Click (object sender, RoutedEventArgs e)
        {
            Process p = new Process();
            try
            {
                p.StartInfo.FileName = "explorer.exe";
                p.StartInfo.Arguments = @"https://github.com/lyz508/Auto-Operation-on-Computer/";
                p.Start();
            }
            catch (System.ComponentModel.Win32Exception ex)
            {
                StatusBar_mainStatus.Items.Clear();
                StatusBar_mainStatus.Items.Add($"{ex.Message}");
            }
        }
    }
}
